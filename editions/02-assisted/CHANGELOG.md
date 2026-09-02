# Журнал изменений

Здесь перечислены заметные изменения TFW Assisted. Номер версии лежит в файле `VERSION`.

Первое число — крупная переделка, второе — добавления, третье — исправления.

## [1.6] — 2026-08-30

Версия 1.6 объединяет field-proven prompt-first/runtime-agnostic исполнение с self-contained prompt-only `tfw-identity` и очистку контракта от ожиданий legacy lifecycle hooks, startup summary, недоступных автоматических проверок и automatic checkpoint. Проверка задачи описана положительно как обязанность активной роли. Исторические функциональные доказательства, допустимые stock SHA-256 и quarantine/delete алгоритм остаются в разделах 1.5 и ниже, `MIGRATION.md` и updater context.

### Добавлено

- Общая prompt-first норма: skills задают результат, инварианты и условия остановки, а ИИ сам выбирает доступные средства; конкретная ОС, Python, Git, shell или исполняемый helper не становятся скрытой зависимостью обычного пользователя.
- Self-contained prompt-only `tfw-identity`, сохраняющий autonomous-role bypass, fail-closed profile/binding validation, surname collision gate, shared-write baseline/post-read, отдельный Assisted namespace и честный session-only fallback.
- Точный маршрут установленного Assisted 1.5 → 1.6 с protected preconditions/postconditions и отдельным доказательством исключения device-local state.
- Публичный нейтральный starter 1.6 — classified derivative полевого поведения 1.6: приватный overlay, персонализированный проект, company identity и local state не входят в пакет.

### Изменено

- `tfw-identity` больше не содержит `scripts/tfw_identity.py` и каталога `scripts/`; пользователь взаимодействует только естественным языком.
- `PROJECT.md`, `AGENTS.md`, `README.md` и текущая процедурная запись описывают task checks как обычный порядок работы без условной рамки недоступных проверок.
- `tfw-update` и его UI metadata сосредоточены на полном version-specific обновлении и protected preservation; legacy cleanup остаётся только во внутренней migration-карте.
- `VERSION` опубликованного набора равен `1.6`.

### Точная migration map 1.5 → 1.6

1. Источник обязан быть целым безопасным пакетом с `VERSION=1.6`, доступным как один exact versioned object и проверенным dynamic observed manifest. Персонализированная папка, частичный набор, package с `project_id`, human profiles, `workspace/`, local bindings или task evidence отклоняется.
2. До единственного Gate updater статически читает пакет без исполнения его кода и показывает source/target service manifests, protected manifest `workspace/`, `knowledge/`, `team/`, изменения service set, exact stock knowledge targets из version-specific карты, сохраняемую персонализацию и local-state exclusion. Неполный package, unsafe link, конфликтный target или изменившийся baseline останавливает запись.
3. Service set заменяется целиком: `AGENTS.md`, `PROJECT.md`, `README.md`, `MIGRATION.md`, `VERSION`, `CHANGELOG.md`, `шаблоны/`, `.agents/skills/`. После замены дословно возвращаются единственный валидный `project_id`, таблица «Карточка проекта», цели, professional AI role и mental model установленного проекта; neutral package ID отсутствует и не копируется.
4. Prompt-only identity overlay обязателен целиком: активные `AGENTS.md`/`README.md`, `.agents/skills/tfw-identity/SKILL.md` и metadata согласованы; `.agents/skills/tfw-identity/scripts/tfw_identity.py`, каталог `scripts/` и активные ссылки на helper отсутствуют. Это не запрещает внутренние инструменты ИИ, но не создаёт runtime-зависимость конечного пользователя.
5. Уже валидные human/automation profile filenames, identifiers и обе role-строки сохраняются без переименования и пересчёта. Missing, duplicate, mixed или invalid profile/project schema блокирует запись; 1.5→1.6 не выполняет profile migration.
6. `workspace/`, `team/` и knowledge сохраняются побайтово, кроме exact stock knowledge targets, названных картой версии и совпавших с опубликованными source-version SHA-256, либо по отдельному records Gate. Приватные имена и hashes не становятся частью публичной нормы; любой другой protected diff является blocker.
7. Local registries TFW Full и Assisted не являются входом или выходом migration: их не читают из package/project root, не копируют между namespace/устройствами, не изменяют, не публикуют и не включают в service/protected/package manifests.
8. Установленный 1.5 не требует legacy cleanup. Точные пути, stock hashes и quarantine/delete алгоритм ранних 1.2/1.3/pre-acceptance 1.4 сохраняются только для version-specific обновления этих источников; они не становятся действующим runtime contract 1.6.
9. После записи обязательны scenarios: uninitialized package; existing/new participant; missing/ambiguous surname; surname collision; shared device; unsafe local store/session-only; autonomous handoff/review; сохранение valid identifiers; отсутствие Full reads/writes, helper и local state в package.
10. Post-manifests должны доказать: `VERSION=1.6`; нулевой необъяснённый protected diff; только разрешённые knowledge changes при выполненных preconditions; совпадение common active/package files кроме доказанно нейтрализованного `PROJECT.md`; неизменность выбранного source object; package cleanliness и внутренние ссылки. Локальный post-read не объявляется доказательством завершённой удалённой синхронизации.

### Protected preconditions и условия остановки

- Установленный проект имеет ровно один marker Assisted / 1.0, `VERSION=1.5`, один canonical UUID `project_id` и валидные profile identifiers/schema.
- Непосредственно перед записью повторяются service/protected manifests и исходные SHA-256. Parallel writer, conflict copy, target collision, изменившийся baseline, невалидная schema, кастомизированный stock target без отдельного решения или необъяснённый protected diff останавливают обновление.
- Карточка проекта, цели, AI role, mental model, owners, task IDs, results, все profiles и все неразрешённые knowledge-файлы являются protected postconditions и должны совпасть с pre-manifest побайтово.

### Clean-package contract 1.6

- `PROJECT.md` имеет `Состояние: НЕ ИНИЦИАЛИЗИРОВАН` и не содержит `project_id` или персонализированную карточку; `team/` содержит только `README.md`.
- Package не содержит `workspace/`, `knowledge/inbox/`, human profiles, machine-local bindings или locks, `.obsidian`, `.codex/`, task/pilot evidence, temp/conflict copies, bytecode, reparse points либо персональные данные проекта.
- `.agents/skills/tfw-identity/` содержит только `SKILL.md` и `agents/openai.yaml`; все TFW skills и metadata проходят структурную проверку; внутренние ссылки существуют.
- Источником поведения является точный field-proven 1.6 snapshot; публичное дерево создаётся как bounded classified derivative. Персонализированная папка не копируется как package source, а выбранный source object остаётся read-only.

## [1.5] — 2026-08-30

Версия 1.5 публикует проверенный multi-user identity contract, разводит machine-local bindings Assisted и TFW Full, вводит surname-based identifiers только для новых human-профилей и поставляется как нейтральный clean starter. Lifecycle hooks по-прежнему не входят в штатный payload; ручной trace/gate порядок остаётся обязательным.

### Добавлено

- Natural-language onboarding для инициализированного и неинициализированного проекта без обязательных команд, identifier, YAML, `project_id` или знания внутреннего устройства TFW.
- Динамический каталог произвольного числа human/automation profiles; универсальный вопрос просит полное имя с фамилией и две роли, но не перечисляет участников.
- Раздельные поля `Роль в компании` и `Роль в проекте`, а также явное разделение current participant, task owner и AI role в trace и отчётах.
- `tfw-identity` со state machine, machine-local multi-project registry, fail-closed schema, exclusive local lock, atomic replace, post-read и narrow create-profile operation.
- Surname-based создание новых human identifiers: кириллица транслитерируется, латиница нормализуется; отсутствующая фамилия и фамильная коллизия требуют смыслового уточнения, а существующий profile/target никогда не перезаписывается.
- Provider-neutral shared-write protocol: target/baseline reread, минимальная запись, post-hash и остановка при конфликте без обещания транзакций или завершённой удалённой синхронизации.
- Нейтральный starter 1.5, собранный из clean 1.4 и проверенного change set без `workspace/`, human profiles, `project_id`, персонализированной карточки, task evidence или local bindings.

### Изменено

- Canonical Assisted binding: `%LOCALAPPDATA%\tfw\assisted\bindings.yml` на Windows и `~/.tfw/assisted/bindings.yml` на POSIX; расположение должно быть доказанно local, safe и reservable.
- Full `bindings.yaml` не читается, не импортируется и не изменяется. Legacy `tfw-assisted/bindings.yml` сохраняется как inert state, но не читается, не мигрирует, не удаляется и не служит fallback; новая запись создаётся после human gate.
- `PROJECT.md` хранит стабильный UUID `project_id` и динамическую ссылку на профили, описывает фактическую shared/local среду, но не хранит current user.
- `AGENTS.md`, `README.md`, `MIGRATION.md`, `team/README.md`, trace template и все lifecycle skills используют одну identity/owner/AI-role, surname/collision и local-state exclusion модель.
- `status` участвует в том же exclusive lock-протоколе, что и записи; единственный профиль без valid binding нигде не выбирается молча.
- `VERSION` опубликованного набора равен `1.5`; marker `1.5-candidate` не является допустимым release source.

### Точная migration map 1.4 → 1.5

1. Источник обязан быть целым нейтральным пакетом с `VERSION=1.5`, полным service manifest и этой картой. `1.5-candidate`, персонализированная проектная папка или частичный набор отклоняются.
2. До единственного Gate updater показывает source/target service manifests, legacy-source protected manifest `work/`, `knowledge/`, `people/` и one-to-one targets `workspace/`, `team/`, exact stock preconditions и local-state exclusion. Код, hooks и scripts источника до Gate не запускаются.
3. Service set заменяется целиком: `AGENTS.md`, `PROJECT.md`, `README.md`, `MIGRATION.md`, `VERSION`, `CHANGELOG.md`, `шаблоны/`, `.agents/skills/`. Карточка проекта, цели, professional AI role и mental model возвращаются дословно; package `project_id` отсутствует и не копируется.
4. Существующий единственный валидный `project_id` сохраняется. Если 1.4-проект не имеет `project_id`, после Gate генерируется новый UUID именно для проекта. Несколько/невалидное значение блокируют запись.
5. Legacy human profile с ровно одним полем `Роль: <текст>` меняется one-to-one на `Роль в компании: <тот же текст>` и `Роль в проекте: не указана`. Уже валидная новая schema, filename и identifier сохраняются, даже если identifier создан по прежней naming-норме. Mixed/duplicate/invalid profile блокирует запись. Переименование filename/identifier допустимо только как отдельное явно согласованное исправление конкретного невалидного профиля с pre/post manifest; массового surname-rename нет.
6. Automation profile переносится one-to-one из legacy-source `people/automation-<slug>.md` в `team/automation-<slug>.md`, сохраняя identifier `automation:<slug>` и обе role строки; human matching его исключает.
7. Full `bindings.yaml`, canonical Assisted `assisted/bindings.yml` и legacy `tfw-assisted/bindings.yml` не являются входом/выходом migration, не входят в manifests и не копируются между namespaces или устройствами. Canonical Assisted entry создаётся отдельно после startup gate.
8. Exact stock knowledge targets обновляются только при source-version SHA-256 из принятой changelog map. Кастомизированный target требует отдельного решения; остальные protected changes должны быть нулевыми.
9. Clean package не добавляет `.codex/`. Если проект пришёл из ранней/pre-acceptance версии с TFW hooks, применяется доказанный stock/quarantine cleanup 1.4 ниже; unrelated `.codex/` сохраняется.
10. После записи обязательны post-manifests и scenarios: uninitialized; 0/1/3/large profiles; existing/new profile; кириллица/латиница; missing surname; surname collision с уточнением; fixed/ask/missing/invalid/duplicate binding; active lock; second computer; shared-store rejection; сохранение valid identifiers; отсутствие Full reads/writes и local state в package.

Коллизия target, изменившийся baseline, conflict copy, parallel writer, неполный package, невалидная profile/project schema или необъяснённый protected diff останавливают обновление; частичное обновление не объявляется успехом.

## [1.4] — 2026-08-24

Версия 1.4 добавляет два режима исполнения TFW, автономную последовательную оркестрацию отдельных Codex-задач, короткие task ID без login владельца и обязательные name/report gates. Исправленный payload временно удаляет экспериментальные lifecycle hooks и возвращает ручную проверку как штатную норму. Независимый review и явная человеческая приёмка перед `done` сохранены.

### Почему hooks удалены

Lifecycle hooks ранних выпусков были тестовыми. На реальной большой папке Stop не укладывался в собственный timeout, а проверочный runner мог зависнуть без полного отчёта. Это не доказанная защита, поэтому `.codex/hooks.json` и оба TFW adapter удалены из clean 1.4 до отдельной будущей задачи переработки; отсутствие startup summary теперь нормально.

### ID и имена Codex-задач

- Новые задачи используют `YYYYMMDD-HHMMSS__slug`; владелец хранится в обязательном поле `Владелец`.
- Slug содержит только строчные латинские буквы, цифры, `.`, `_`, `-`, начинается с буквы/цифры и не содержит `__`. Коллизия требует нового фактического timestamp; reuse/overwrite запрещены.
- Legacy-ID `YYYYMMDD-HHMMSS__handle__slug` и стабильные пути не переименовываются; skills и ручная проверка принимают обе схемы.
- Обязательные точные имена: `plan | <ID>`, `handoff | <ID>`, `review | <ID>`. Для legacy только видимое имя исключает средний handle. Невозможность установить/проверить имя блокирует содержательную работу.

### Режимы, отчёты и gates

- Gate 0 фиксирует `Режим исполнения: ручной | автономный`.
- В ручном режиме пользователь запускает следующий чат по точной команде.
- В автономном режиме plan после отдельного ограниченного разрешения создаёт и последовательно контролирует handoff/review только текущего task ID, при `FAIL` запускает новый handoff и review, а после `PASS` выносит человеку один пакет.
- Одновременно task folder пишет одна роль; plan не редактирует trace во время handoff/review; reviewer не исправляет результат.
- Handoff/review отправляют coordinator thread обязательные preflight, exception и final reports. Отсутствие отчёта, неверное имя или расхождение с trace не являются завершением этапа.
- Если task/thread-операции недоступны, plan честно использует ручной fallback. TFW не обещает работу при закрытом провайдере, безопасную параллельную запись или завершённую удалённую синхронизацию.
- Перед финальной приёмкой knowledge decision фактически исполнен и проверен. Только явное решение человека после независимого `PASS` допускает изменение только `review → done`.

### Точная migration map 1.3 → 1.4

1. Пользователь пишет: `Используй /tfw-update и обнови этот проект из доверенного пакета 1.4 <точный путь, архив, URL или объект>`.
2. Установленный prompt-only updater 1.3 статически проверяет целый пакет и до одного Gate показывает service manifest и version-specific protected migration.
3. Service set заменяется целиком: `AGENTS.md`, `PROJECT.md`, `README.md`, `MIGRATION.md`, `VERSION`, `CHANGELOG.md`, `шаблоны/`, `.agents/skills/`. Clean package не несёт `.codex/`; в существующей `.codex/` выполняется только version-specific TFW hook cleanup, unrelated content сохраняется. Карточка проекта, профессиональная роль и ментальная модель возвращаются дословно.
4. Существующие legacy-source `work/<legacy-ID>/` переносятся one-to-one в `workspace/<legacy-ID>/`; ID, владельцы, результаты и история не переписываются.
5. Exact stock knowledge targets заменяются только при source-version SHA-256 из принятой changelog map; приватные имена и hashes не публикуются как общая норма.
6. Кастомизированный protected-файл требует отдельного решения. Все остальные existing `knowledge/` сохраняются; legacy-source `work/` и `people/` сопоставляются one-to-one с `workspace/` и `team/`.
7. Post-manifest, новый/legacy ID, name/report/knowledge scenarios, skills/metadata, ручные links/secret checks, отсутствие активной TFW-регистрации и доказательство stock/custom cleanup обязательны.

### Точная migration map 1.2 → 1.4

1. Пользователь пишет: `Примени .agents/skills/tfw-update/SKILL.md из доверенного пакета 1.4 <точный путь, архив, URL или объект> к этому проекту 1.2 и выполни прямое обновление до 1.4`.
2. Договор updater берётся из целого проверенного пакета 1.4: локальный updater 1.2 запрещает protected migration и не может быть основанием полного прямого обновления.
3. До единственного Gate показываются service manifest, protected manifest и one-to-one карта legacy-source `work/<status>/<legacy-ID>/ → workspace/<legacy-ID>/`.
4. Service set заменяется 1.4 с дословным возвратом карточки, роли и ментальной модели.
5. Task folder переносится только при уникальном ID, совпадении полей ID/статуса, существующем trace и свободном target. ID и пользовательские артефакты не меняются.
6. В traces нормализуются только обязательные поля и живые пути `work/<status>/<ID>/ → workspace/<ID>/`; историческое описание остаётся provenance. Для `review`/`done` результат существует.
7. Exact stock knowledge targets обновляются только при source-version hashes из принятой changelog map и совпавшем baseline.
8. Все прочие protected-файлы сохраняются побайтово. Missing, unexpected и необъяснённых changes должно быть ноль.

Коллизия, несовпадение ID/статуса, параллельная запись, неполный пакет, изменённый stock-файл или неописанная protected migration останавливают обновление до записи; частичное обновление не объявляется успехом.

### Экспериментальные hooks временно удалены

Исправленный clean 1.4 не содержит `.codex/hooks.json`, `.codex/hooks/tfw-hook.ps1` и `.codex/hooks/tfw-hook.sh` и не обещает SessionStart, PreCompact или Stop. Перед сокращением контекста и завершением действует ручной порядок из `README.md`.

| Source | `hooks.json` | `tfw-hook.ps1` | `tfw-hook.sh` |
|---|---|---|---|
| 1.2 | `044013a5cb31ca8c29708b0f83d5ef0e53aecb83d12091c60434a750735043ce` | `85191702eef52dc5191e27485ac50c8e27dd334e2a6bc30d82d14711829361c7` | `18039f1631375d7bea2332ffa0c55fdb602315d69ffa98f76f3875fca9eb5a1a` |
| 1.3 | `c09d0de4c7043691d9cbbae270aaa058793e9e1503d39d4f177937d938a6e374` | `c09e9ac226e242075ab2d06fd8bedd2ae24a0c0efd3e45676978a3f34ab43842` | `c21e2cf54566f9a3ea02f769a7bd11af1ccec046a4a66cc135ded614386fda86` |
| pre-acceptance 1.4 | `c09d0de4c7043691d9cbbae270aaa058793e9e1503d39d4f177937d938a6e374` | `c29b66b3565741d9b86e76a24ad8620b9809f8c6682f630c7564315ef9e2d58d` | `e05076eeae03b980f9db7d0ccac02ad859e7a56c5393d06e3245d4dfd94ae49a` |

После единственного Gate exact stock удаляется автоматически без второго вопроса. Hash mismatch запрещает silent delete: modified adapter сначала сохраняется побайтово как `.codex/tfw-quarantine/<source-version>/<sha256-prefix>-<basename>` с полным hash в отчёте, затем удаляется из активного штатного пути. Custom valid `hooks.json` также quarantined целиком; из активной копии удаляются только command-объекты, ссылающиеся на TFW adapters, а unrelated hook entries/top-level fields и другие `.codex`-файлы сохраняются. Invalid JSON, неоднозначная структура или quarantine collision с иным содержимым останавливают запись.

Same-version correction уже установленной pre-acceptance 1.4 использует ту же карту и не является новым функциональным upgrade. Отдельная задача переработки hooks находится вне scope 1.4.

### Центральный релиз

Публичный Assisted 1.4 был собран из принятой нейтральной 1.3 и проверенного change set. Он не содержит legacy TFW hook payload, `workspace/`, human profiles, персонализированную карточку, `knowledge/inbox/` или task evidence. Прямые маршруты проверяются на изолированных персонализированных фикстурах с manifests до/после; исходные releases остаются неизменными.

## [1.3] — 2026-08-24

Версия 1.3 переводит задачи на стабильный путь и соединяет четыре команды в один проверяемый цикл: планирование, исполнение, независимое review и явная человеческая приёмка.

### Причина

В версии 1.2 статус задачи кодировался в родительском каталоге. Переход между `doing`, `review` и `done` перемещал task folder, менял адрес trace и результата и мог оставить несуществующую ссылку после `tfw-review FAIL`.

### Добавлено

- `/tfw-handoff` исполняет согласованный Gate 0, ведёт единственный trace, самопроверяет DoD/DoF и меняет только `Статус: doing → review`.
- `/tfw-review` в новом чате независимо повторяет проверки. `PASS` оставляет `review`; `FAIL` меняет только `review → doing`; результат и task folder не перемещаются.
- Все четыре skill folders содержат согласованные `agents/openai.yaml`.
- `/tfw-update` является переносимым prompt-only skill: его папка содержит только `SKILL.md` и `agents/openai.yaml`, без собственного Python, shell helper, downloader или unpacker. ИИ сам выбирает доступные инструменты текущей среды для пути, архива, URL, облачной ссылки, вложения или иной формы источника и соблюдает единые инварианты проверки независимо от способа доступа.

### Изменено

- Каждая задача живёт на одном адресе `work/<ID>/`; статус хранится только в поле `Статус` внутри `TRACE.md`.
- `/tfw-plan → /tfw-handoff → /tfw-review → человеческая приёмка` — обязательная последовательность. Только человек после независимого `PASS` может установить `done`.
- `AGENTS.md`, `README.md`, `MIGRATION.md`, пять skills, `team/README.md`, шаблон плана и active paths `workspace/`/`knowledge/` согласованы со stable-path моделью.
- PowerShell- и POSIX-hooks считают статусы по traces, выбирают actor-scoped `doing`-задачу, идемпотентно checkpoint-ят только её и проверяют обязательные поля, допустимый статус, существование результатов и внутренних ссылок; документированный шаблон будущего кандидата `knowledge/inbox/YYYYMMDD-HHMMSS__handle__slug.md` не считается битой живой ссылкой до создания кандидата.

### Точные правила обновления 1.2 → 1.3

До единственного согласования `/tfw-update` обязан получить источник в безопасную временную рабочую область доступными средствами текущей среды, статически проверить пакет и показать версии, service manifest и следующую protected migration map. Конкретная ОС, runtime, оболочка, архиватор, браузер или коннектор не являются частью контракта. Код, hooks и scripts источника до согласования не запускаются.

1. **Служебный набор заменяется целиком:** `AGENTS.md`, `PROJECT.md`, `README.md`, `MIGRATION.md`, `VERSION`, `CHANGELOG.md`, `шаблоны/`, `.agents/skills/`, `.codex/`. Таблица «Карточка проекта» и две строки раздела «Настройка этого проекта» возвращаются дословно; маркеры Assisted / 1.0 сохраняются.
2. **Manifest до записи:** фиксируются legacy-source `work/`/`people/`, `knowledge/` и их one-to-one targets `workspace/`/`team/` по относительному пути, размеру и SHA-256. Перед применением исходные хэши проверяются повторно.
3. **One-to-one миграция задач:** каждый direct legacy-source task folder `work/<status>/<ID>/` переносится в `workspace/<ID>/` только если ID уникален, target отсутствует, `TRACE.md` существует, поле `ID задачи` совпадает с папкой, а поле `Статус` совпадает с исходным status-каталогом. ID и пользовательские артефакты не меняются.
4. **Разрешённые изменения traces:** только нормализация обязательных полей без изменения смысла и замена живых путей `work/<status>/<ID>/` на `workspace/<ID>/` в поле `Результат` и актуальных ссылках. Историческое описание прежней схемы сохраняется и помечается как legacy. Для `review` и `done` итоговый результат существует.
5. **Stock knowledge:** exact target заменяется версией назначения только при source-version SHA-256 из принятой changelog map. Изменённый пользователем файл считается конфликтом и не перезаписывается без отдельного решения.
6. **Остальные защищённые материалы неизменны:** другие файлы `knowledge/`, все target-профили `team/` и пользовательские артефакты в `workspace/` совпадают по SHA-256, кроме отдельно показанных trace-изменений.
7. **Manifest после записи:** отсутствующие, неожиданные и необъяснённо изменённые защищённые файлы должны быть равны нулю. Каждое разрешённое изменение перечисляется по пути и SHA-256 до/после.

Коллизия ID/пути, несовпадение статуса, параллельное изменение, небезопасный архив, неполный пакет или кастомизированная процедурная запись останавливают обновление до записи либо до затрагивания конфликтного файла. Частичное обновление не объявляется успехом.

### Источники обновления и честные границы

- Путь, архив, URL, облачная ссылка, вложение и иное доступное представление одной версии должны приводить к одному файловому дереву по SHA-256 manifest; способ получения выбирает ИИ из реально доступных инструментов.
- Если источник не дан, ИИ задаёт один короткий вопрос о его расположении. Если ссылка закрыта, авторизация или нужный способ доступа недоступны, архив повреждён либо пакет неполон, ИИ называет точную причину и просит доступное представление или экспорт без изменения проекта; обход авторизации не обещается.
- В URL, trace и отчёт не записываются токены и query-параметры доступа.
- Проверка локальных файлов не доказывает завершение удалённой синхронизации выбранного провайдера.
- Assisted не гарантирует безопасное одновременное редактирование одного trace.
- После изменения `AGENTS.md` требуется новая сессия; после изменения hooks человек заново просматривает определения и подтверждает доверие.

## [1.2] — 2026-08-12

### Добавлено

- **Команда `/tfw-plan`** — `.agents/skills/tfw-plan/SKILL.md`. Заводит задачу, читает файлы папки в заданном порядке, заполняет план работы по шаблону и останавливается на согласовании.
- **Команда `/tfw-update`** — `.agents/skills/tfw-update/SKILL.md`. Обновляет служебные файлы папки до новой версии. Задачи, знания и профили не трогает.
- **Файл `VERSION`** — номер версии одной строкой. По нему видно, какая версия у вас на руках.
- **Файл `CHANGELOG.md`** — этот журнал. По нему видно, что изменилось между версиями.
- **Раздел «Команды» в `README.md`** — как вызвать команду и как написать свою.
- **Раздел «Команды» в `AGENTS.md`** — правило для помощника: команду из `.agents/skills/` выполнять по её файлу.

### Изменено

- **`PROJECT.md`** — добавлена строка «Версия папки» со ссылкой на файл `VERSION`. Строки «Активная редакция» и «Версия редакции» остались нетронутыми: их читают служебные проверки.
- **`AGENTS.md`, раздел «При старте»** — помощник берёт номер версии папки из файла `VERSION`, а состав изменений — отсюда.

### Правила обновления до этой версии

Эти правила обязательны и относятся к самому обновлению, а не к работе после него.

1. **Обновление выполняет помощник целиком.** Пользователь соглашается один раз, увидев список изменений. Ручных шагов после этого не остаётся. Список «скопируйте это сами» — признак незаконченного обновления.
2. **Папки `.agents/skills/` и `.codex/` входят в обновление.** Их копирует помощник вместе с остальным. Отдельного действия пользователя они не требуют.
3. **Строки `Активная редакция: Assisted` и `Версия редакции: 1.0` в `PROJECT.md` сохраняются дословно.** Updater проверяет их как устойчивые markers совместимости; версия папки живёт отдельной строкой и в `VERSION`.
4. **Заполненное пользователем переносится дословно:** раздел «Настройка этого проекта» в `AGENTS.md` и таблица «Карточка проекта» в `PROJECT.md`.
5. **После обновления помощник отчитывается числами:** сколько файлов в `workspace/`, `knowledge/`, `team/` и сколько из них необъяснённо изменено — последнее число должно быть нулём.

### Причина

Полевое использование показало: помощник не всегда соблюдает порядок работы, если этого не потребовать явно. Просьба словами каждый раз звучит по-разному, и результат тоже разный. Команда — это записанная один раз просьба, которая выполняется одинаково.

## [1.1] — 2026-08-11

### Добавлено

- Field overlay поверх TFW Assisted: заполненный проектный контекст, private knowledge и company identity оставались downstream; публичная производная сохраняет документ A4, заметку, план работы, презентацию и сборщик `build_a4.py` в нейтральном виде.

Версия прошла полевое использование и стала behavioral source для публичной нейтральной производной.

## [1.0]

### Добавлено

- Базовая редакция TFW Assisted: `AGENTS.md`, `README.md`, `PROJECT.md`, `MIGRATION.md`, `knowledge/INDEX.md`, `team/README.md` и prompt-only skills без shipped lifecycle runtime.
