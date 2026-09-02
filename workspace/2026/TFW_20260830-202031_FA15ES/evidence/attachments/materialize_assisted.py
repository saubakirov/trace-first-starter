"""Materialize the frozen Assisted 1.6 derivative from the read-only field source.

This task-local evidence helper is not shipped in the product. It refuses source
drift, verifies that replacements cover exactly the frozen 205 source lines, keeps
source line endings and every unlisted source line byte-identical, and writes only
the fixed product paths declared by TS TFW_20260830-202031_FA15ES.
"""

from __future__ import annotations

import hashlib
import os
import subprocess
from pathlib import Path


TASK_ID = "TFW_20260830-202031_FA15ES"
EXPECTED_BRANCH = "codex/tfw-fa15es-executor"
SOURCE = Path(os.environ["TFW_FA15ES_SOURCE"])
REPO = Path(__file__).resolve().parents[5]
TARGET = REPO / "editions" / "02-assisted"


SOURCE_BASELINES = {
    ".agents/skills/tfw-handoff/agents/openai.yaml": (378, "0516336e97d6"),
    ".agents/skills/tfw-handoff/SKILL.md": (11114, "ee4c703bee29"),
    ".agents/skills/tfw-identity/agents/openai.yaml": (547, "cd2acda1961b"),
    ".agents/skills/tfw-identity/SKILL.md": (18464, "5e0723a44333"),
    ".agents/skills/tfw-plan/agents/openai.yaml": (330, "9d1f968f1eae"),
    ".agents/skills/tfw-plan/SKILL.md": (12994, "b5e0b78448ca"),
    ".agents/skills/tfw-review/agents/openai.yaml": (344, "a7db8ffe61ad"),
    ".agents/skills/tfw-review/SKILL.md": (10643, "c56e0089282a"),
    ".agents/skills/tfw-update/agents/openai.yaml": (454, "f17f189f8fac"),
    ".agents/skills/tfw-update/SKILL.md": (22251, "416a768c20f9"),
    "AGENTS.md": (31319, "79cd1e6bac0b"),
    "CHANGELOG.md": (43630, "a1aa3b04fa8c"),
    "knowledge/INDEX.md": (3701, "2b143d09efb3"),
    "MIGRATION.md": (21271, "1bf711f1280b"),
    "people/README.md": (6283, "10ec126927ec"),
    "PROJECT.md": (9124, "d1d8eb93ce61"),
    "README.md": (19824, "090d419abdfa"),
    "VERSION": (4, "e5cd57eee963"),
    "шаблоны/build_a4.py": (7298, "ab18472ca1aa"),
    "шаблоны/документ_A4.md": (5270, "b3638c2f3289"),
    "шаблоны/заметка.md": (3293, "ad5228af1466"),
    "шаблоны/план_работы.md": (7790, "03820291852c"),
    "шаблоны/презентация.html": (25557, "fb4012fe3733"),
}


EXACT = {
    ".agents/skills/tfw-handoff/agents/openai.yaml": ".agents/skills/tfw-handoff/agents/openai.yaml",
    ".agents/skills/tfw-identity/agents/openai.yaml": ".agents/skills/tfw-identity/agents/openai.yaml",
    ".agents/skills/tfw-plan/agents/openai.yaml": ".agents/skills/tfw-plan/agents/openai.yaml",
    ".agents/skills/tfw-review/agents/openai.yaml": ".agents/skills/tfw-review/agents/openai.yaml",
    ".agents/skills/tfw-update/agents/openai.yaml": ".agents/skills/tfw-update/agents/openai.yaml",
    "VERSION": "VERSION",
}


ADAPTED_TARGETS = {
    ".agents/skills/tfw-plan/SKILL.md": ".agents/skills/tfw-plan/SKILL.md",
    ".agents/skills/tfw-handoff/SKILL.md": ".agents/skills/tfw-handoff/SKILL.md",
    ".agents/skills/tfw-review/SKILL.md": ".agents/skills/tfw-review/SKILL.md",
    ".agents/skills/tfw-update/SKILL.md": ".agents/skills/tfw-update/SKILL.md",
    ".agents/skills/tfw-identity/SKILL.md": ".agents/skills/tfw-identity/SKILL.md",
    "AGENTS.md": "AGENTS.md",
    "CHANGELOG.md": "CHANGELOG.md",
    "knowledge/INDEX.md": "knowledge/INDEX.md",
    "MIGRATION.md": "MIGRATION.md",
    "people/README.md": "team/README.md",
    "PROJECT.md": "PROJECT.md",
    "README.md": "README.md",
    "шаблоны/build_a4.py": "шаблоны/build_a4.py",
    "шаблоны/документ_A4.md": "шаблоны/документ_A4.md",
    "шаблоны/заметка.md": "шаблоны/заметка.md",
    "шаблоны/план_работы.md": "шаблоны/план_работы.md",
    "шаблоны/презентация.html": "шаблоны/презентация.html",
}


REPLACEMENTS: dict[str, dict[int, str]] = {
    ".agents/skills/tfw-plan/SKILL.md": {
        21: "3. Атомарно создай только отсутствующую папку `workspace/<ID>/`. Если путь уже существует, не переиспользуй и не перезаписывай его: получи новый фактический timestamp и повтори создание.",
        29: "1. Создай `workspace/<ID>/TRACE.md` с начальным `Статус: doing` и отдельными полями `Владелец`, `Текущий участник: <identifier>`, `Корпоративная роль текущего участника`, `Проектная роль текущего участника` и `Роль ИИ: plan`.",
    },
    ".agents/skills/tfw-handoff/SKILL.md": {
        12: "- Путь задачи всегда `workspace/<ID>/` и не меняется при переходах статуса.",
        30: "1. Для явного пути проверь, что он разрешается в непосредственную task folder внутри `workspace/`, имя папки равно ID из trace и существует `TRACE.md`.",
        31: "2. Для явного ID найди ровно одну папку `workspace/<ID>/`; не выбирай по частичному совпадению и не ищи в legacy-каталогах статусов.",
    },
    ".agents/skills/tfw-review/SKILL.md": {
        12: "- Путь задачи всегда `workspace/<ID>/` и не меняется при `PASS`, `FAIL` или человеческой приёмке.",
        31: "1. Для пути проверь, что он разрешается в непосредственную task folder внутри `workspace/`, содержит `TRACE.md`, имя папки равно ID и `Статус: review`.",
        32: "2. Для ID найди ровно одну `workspace/<ID>/`; не выбирай частичное совпадение и не ищи в статусных каталогах.",
    },
    ".agents/skills/tfw-update/SKILL.md": {
        3: "description: Команда /tfw-update получает целый пакет TFW, проверяет version-specific migration и после одного согласования обновляет service set, сохраняя project identity, персонализацию, valid profile identifiers, workspace/knowledge/team и исключая device-local bindings Full/Assisted; применяет только доказанную migration map.",
        18: "`workspace/`, `knowledge/`, `team/` не меняются, если migration конкретной версии одновременно не:",
        43: "2. Статически прочитай service set, все `tfw-*` skills и metadata. Убедись, что `.agents/skills/tfw-update/` содержит только `SKILL.md` и `agents/openai.yaml`, а clean package не содержит `.codex/`, `workspace/`, inbox, human profiles, `project_id`, персонализированную карточку, task/pilot evidence, local binding registry, temp/conflict copies или reparse points; `PROJECT.md` обязан быть `НЕ ИНИЦИАЛИЗИРОВАН`. Для 1.6 дополнительно проверь, что `tfw-identity` содержит только `SKILL.md` и `agents/openai.yaml`, без helper и `scripts/`.",
        45: "4. Составь manifest всех `workspace/`, `knowledge/`, `team/`; повторно сними его непосредственно перед записью.",
        53: "- `workspace/`, `team/` и knowledge сохраняются побайтово, кроме точных stock knowledge targets, названных version-specific картой пакета и совпавших с опубликованными исходными SHA-256, либо по отдельному точному records Gate; приватные имена и хэши не становятся общей нормой;",
        57: "- postconditions: `VERSION=1.6`, uninitialized clean package, нулевой необъяснённый protected diff, только точные разрешённые knowledge changes при выполненных preconditions, сохранение персонализации/valid identifiers и common active/package equality кроме нейтрализованного `PROJECT.md`;",
        64: "- карточка проекта, цели, knowledge, legacy-source `work/` с one-to-one target `workspace/`, task IDs, владельцы, professional AI role и mental model сохраняются;",
        67: "- stock knowledge targets обновляются только при exact source-version SHA-256 из changelog либо по отдельному точному records Gate; приватные имена и digests в публичный договор не встраиваются;",
        68: "- local bindings TFW Full и legacy Assisted `tfw-assisted/bindings.yml` не читаются, не мигрируют и не входят в manifests; canonical Assisted использует `%LOCALAPPDATA%\\tfw\\assisted\\bindings.yml` или `~/.tfw/assisted/bindings.yml` и создаёт запись заново через human gate;",
        73: "- существующий legacy-source `work/<legacy-ID>/` переносится one-to-one в `workspace/<legacy-ID>/`; ID, trace semantics и история не переписываются;",
        74: "- stock knowledge targets заменяются только при совпадении известных исходных SHA-256 из changelog, без публикации приватных имён в общей карте;",
        81: "- каждый прямой legacy-source `work/<status>/<legacy-ID>/` переносится one-to-one в `workspace/<legacy-ID>/` только при уникальном ID, совпадении ID/статуса, существующем trace и свободном target;",
        82: "- в traces допустимы только нормализация обязательных полей и живых путей `work/<status>/<ID>/ → workspace/<ID>/`; историческое описание не переписывается;",
        83: "- stock knowledge targets обновляются только при exact source-version hashes из changelog и отдельной проверке preconditions;",
    },
    ".agents/skills/tfw-identity/SKILL.md": {
        23: "3. Динамически прочитай `team/*.md`, кроме `README.md`. Каждый human-профиль должен иметь ровно по одному полю `Идентификатор`, `Отображаемое имя`, `Тип: человек`, `Роль в компании`, `Роль в проекте`; filename совпадает с identifier, а identifier соответствует `^[a-z0-9][a-z0-9_-]*$`. Automation-профиль имеет `Тип: automation`, identifier `automation:<slug>`, filename `automation-<slug>.md` и обе role-строки; валидируй его, но исключай из human matching. Duplicate identifier, неоднозначное нормализованное отображаемое имя, missing/duplicate field или неверная schema блокируют выбор и запись. Уже валидные identifiers не пересчитывай.",
        46: "1. Сними manifest всех `team/*.md` как упорядоченные `relative path + size + SHA-256`, перечитай все human-профили и проверь отсутствие точного target. Непосредственно перед записью повтори manifest и target-read; любое расхождение, conflict copy или признак другого писателя останавливает запись.",
        47: "2. Создай исключительно новый `team/<identifier>.md`, никогда не открывая существующий target на overwrite. Файл содержит ровно по одному полю:",
        59: "3. После записи перечитай файл и manifest. Должен появиться ровно один ожидаемый path с SHA-256 ожидаемого содержимого, а все прежние entries должны совпасть. При расхождении не выполняй merge и не продолжай к local binding; сообщи конфликт. Local post-read не доказывает завершённую удалённую синхронизацию выбранного shared-хранилища.",
        63: "Выбери безопасный machine-local TFW family root вне project/shared/sync roots и используй отдельный Assisted child `assisted/bindings.yml`; точные платформенные пути указаны ниже. Не требуй от пользователя находить путь или запускать команды. Reject symlink/reparse наружу, shared path, unreadable/non-regular state и любое расположение, безопасность которого не доказана.",
        67: "- Windows: `%LOCALAPPDATA%\\tfw\\assisted\\bindings.yml`;",
        68: "- macOS: `~/.tfw/assisted/bindings.yml` как явное исключение TFW family root;",
        69: "- Linux/Unix: `~/.tfw/assisted/bindings.yml` как явное исключение TFW family root.",
        85: "- Namespace TFW Full (`%LOCALAPPDATA%\\tfw\\bindings.yaml` или `~/.tfw/bindings.yaml`) не читай, не импортируй и не изменяй. Legacy Assisted `tfw-assisted/bindings.yml` сохрани как inert state, но никогда не читай, не мигрируй, не удаляй и не используй как fallback.",
    },
    "AGENTS.md": {
        20: "- Профессиональная роль ИИ: рабочий помощник проекта — готовит документы, разбирает материалы, ведёт задачу и её след. О проекте отвечает только по файлам `knowledge/records/`; чего там нет — говорит, что нет.",
        41: "- Обнаруживай профили динамически в `team/*.md`, исключая `README.md`; не зашивай имена или предел количества участников.",
        49: "Локальный выбор является заявленной атрибуцией, а не аутентификацией или подтверждением полномочий. Assisted хранит только `project_id`, режим и identifier участника в `%LOCALAPPDATA%\\tfw\\assisted\\bindings.yml` на Windows или `~/.tfw/assisted/bindings.yml` на POSIX; роли читаются из профиля. Full `bindings.yaml` и legacy `tfw-assisted/bindings.yml` не читаются, не импортируются и не изменяются. Если безопасное несинхронизируемое расположение или запись не доказаны, продолжай только session-only и честно сообщи простыми словами, что выбор не удалось запомнить на следующий раз.",
        62: "2. создай по одному профилю человека по `team/README.md`, разделяя роль в компании и роль в проекте и не сохраняя лишние персональные данные;",
        81: "- `/tfw-update` после одного согласования обновляет служебный набор целиком. `workspace/`, `knowledge/` и `team/` защищены, кроме явно описанной в changelog и отдельно согласованной миграции с manifest до/после.",
        86: "Только явная человеческая приёмка после независимого `PASS` позволяет установить `Статус: done`. Смена статуса никогда не перемещает task folder: одна задача всегда живёт на `workspace/<ID>/`.",
        118: "2. Определи автора через Gate текущего участника. Валидная machine-local привязка позволяет продолжить независимо от числа профилей; без неё используй тот же короткий onboarding даже при одном профиле, потому что на новом или общем устройстве человек может быть новым участником. Не перечисляй большой список и не проси у человека handle, путь или формат; после ответа сам выполни допустимую локальную запись либо включи режим общего компьютера. Для автоматизации допустим отдельный профиль `automation:<slug>` по `team/README.md`; автономная task-роль наследует владельца из trace и не имитирует человеческую идентификацию.",
        119: "3. Создай только отсутствующую папку задачи `workspace/<ID>/`, где новый ID — `YYYYMMDD-HHMMSS__slug`, без login/handle. Slug начинается с строчной латинской буквы или цифры, содержит только `.`, `_`, `-`, строчные латинские буквы и цифры; последовательность `__` запрещена для однозначного отличия от legacy-ID. При коллизии не переиспользуй и не перезаписывай путь: возьми новый фактический timestamp. Существующие legacy-папки `YYYYMMDD-HHMMSS__handle__slug` переносятся только по точной version-specific карте.",
        121: "5. Создай `workspace/<ID>/TRACE.md` до результата. Запиши поля:",
        129: "Одна задача и её изменяемый trace имеют одного владельца записи и одного активного писателя этапа. Не создавай общий task board, общий счётчик или `CURRENT_USER`. Статус меняется только в поле `Статус`; папка задачи остаётся на стабильном пути `workspace/<ID>/`. Переход в `review` или `done` допустим только с существующим путём результата от корня проекта.",
        145: "Этот проект может находиться в локальном или синхронизируемом shared-хранилище и открываться на разных компьютерах. Синхронизация может быть eventual: локальный post-read или hash подтверждает только видимую копию и не доказывает завершённую удалённую синхронизацию.",
        148: "- Новый человек получает отдельный surname-based `team/<identifier>.md`; onboarding не переписывает `PROJECT.md`, общую карточку или `knowledge/`. Существующий valid identifier не пересчитывается; missing surname или коллизия требует уточнения до записи.",
        149: "- Один изменяемый trace в `workspace/<ID>/` имеет одного активного писателя этапа. Lock, локальный hash или клиент синхронизации не являются доказательством безопасной параллельной записи.",
        159: "- trace существует на `workspace/<ID>/TRACE.md`;",
        164: "- внутренние ссылки на `workspace/`, `knowledge/`, `team/` и `шаблоны/` существуют;",
    },
    "CHANGELOG.md": {
        3: "Здесь перечислены заметные изменения TFW Assisted. Номер версии лежит в файле `VERSION`.",
        9: "Версия 1.6 объединяет field-proven prompt-first/runtime-agnostic исполнение с self-contained prompt-only `tfw-identity` и очистку контракта от ожиданий legacy lifecycle hooks, startup summary, недоступных автоматических проверок и automatic checkpoint. Проверка задачи описана положительно как обязанность активной роли. Исторические функциональные доказательства, допустимые stock SHA-256 и quarantine/delete алгоритм остаются в разделах 1.5 и ниже, `MIGRATION.md` и updater context.",
        16: "- Публичный нейтральный starter 1.6 — classified derivative полевого поведения 1.6: приватный overlay, персонализированный проект, company identity и local state не входят в пакет.",
        27: "1. Источник обязан быть целым безопасным пакетом с `VERSION=1.6`, доступным как один exact versioned object и проверенным dynamic observed manifest. Персонализированная папка, частичный набор, package с `project_id`, human profiles, `workspace/`, local bindings или task evidence отклоняется.",
        28: "2. До единственного Gate updater статически читает пакет без исполнения его кода и показывает source/target service manifests, protected manifest `workspace/`, `knowledge/`, `team/`, изменения service set, exact stock knowledge targets из version-specific карты, сохраняемую персонализацию и local-state exclusion. Неполный package, unsafe link, конфликтный target или изменившийся baseline останавливает запись.",
        32: "6. `workspace/`, `team/` и knowledge сохраняются побайтово, кроме exact stock knowledge targets, названных картой версии и совпавших с опубликованными source-version SHA-256, либо по отдельному records Gate. Приватные имена и hashes не становятся частью публичной нормы; любой другой protected diff является blocker.",
        36: "10. Post-manifests должны доказать: `VERSION=1.6`; нулевой необъяснённый protected diff; только разрешённые knowledge changes при выполненных preconditions; совпадение common active/package files кроме доказанно нейтрализованного `PROJECT.md`; неизменность выбранного source object; package cleanliness и внутренние ссылки. Локальный post-read не объявляется доказательством завершённой удалённой синхронизации.",
        46: "- `PROJECT.md` имеет `Состояние: НЕ ИНИЦИАЛИЗИРОВАН` и не содержит `project_id` или персонализированную карточку; `team/` содержит только `README.md`.",
        47: "- Package не содержит `workspace/`, `knowledge/inbox/`, human profiles, machine-local bindings или locks, `.obsidian`, `.codex/`, task/pilot evidence, temp/conflict copies, bytecode, reparse points либо персональные данные проекта.",
        49: "- Источником поведения является точный field-proven 1.6 snapshot; публичное дерево создаётся как bounded classified derivative. Персонализированная папка не копируется как package source, а выбранный source object остаётся read-only.",
        62: "- Provider-neutral shared-write protocol: target/baseline reread, минимальная запись, post-hash и остановка при конфликте без обещания транзакций или завершённой удалённой синхронизации.",
        63: "- Нейтральный starter 1.5, собранный из clean 1.4 и проверенного change set без `workspace/`, human profiles, `project_id`, персонализированной карточки, task evidence или local bindings.",
        67: r"- Canonical Assisted binding: `%LOCALAPPDATA%\tfw\assisted\bindings.yml` на Windows и `~/.tfw/assisted/bindings.yml` на POSIX; расположение должно быть доказанно local, safe и reservable.",
        68: "- Full `bindings.yaml` не читается, не импортируется и не изменяется. Legacy `tfw-assisted/bindings.yml` сохраняется как inert state, но не читается, не мигрирует, не удаляется и не служит fallback; новая запись создаётся после human gate.",
        69: "- `PROJECT.md` хранит стабильный UUID `project_id` и динамическую ссылку на профили, описывает фактическую shared/local среду, но не хранит current user.",
        70: "- `AGENTS.md`, `README.md`, `MIGRATION.md`, `team/README.md`, trace template и все lifecycle skills используют одну identity/owner/AI-role, surname/collision и local-state exclusion модель.",
        77: "2. До единственного Gate updater показывает source/target service manifests, legacy-source protected manifest `work/`, `knowledge/`, `people/` и one-to-one targets `workspace/`, `team/`, exact stock preconditions и local-state exclusion. Код, hooks и scripts источника до Gate не запускаются.",
        81: "6. Automation profile переносится one-to-one из legacy-source `people/automation-<slug>.md` в `team/automation-<slug>.md`, сохраняя identifier `automation:<slug>` и обе role строки; human matching его исключает.",
        82: "7. Full `bindings.yaml`, canonical Assisted `assisted/bindings.yml` и legacy `tfw-assisted/bindings.yml` не являются входом/выходом migration, не входят в manifests и не копируются между namespaces или устройствами. Canonical Assisted entry создаётся отдельно после startup gate.",
        83: "8. Exact stock knowledge targets обновляются только при source-version SHA-256 из принятой changelog map. Кастомизированный target требует отдельного решения; остальные protected changes должны быть нулевыми.",
        111: "- Если task/thread-операции недоступны, plan честно использует ручной fallback. TFW не обещает работу при закрытом провайдере, безопасную параллельную запись или завершённую удалённую синхронизацию.",
        116: "1. Пользователь пишет: `Используй /tfw-update и обнови этот проект из доверенного пакета 1.4 <точный путь, архив, URL или объект>`.",
        119: "4. Существующие legacy-source `work/<legacy-ID>/` переносятся one-to-one в `workspace/<legacy-ID>/`; ID, владельцы, результаты и история не переписываются.",
        120: "5. Exact stock knowledge targets заменяются только при source-version SHA-256 из принятой changelog map; приватные имена и hashes не публикуются как общая норма.",
        121: "6. Кастомизированный protected-файл требует отдельного решения. Все остальные existing `knowledge/` сохраняются; legacy-source `work/` и `people/` сопоставляются one-to-one с `workspace/` и `team/`.",
        126: "1. Пользователь пишет: `Примени .agents/skills/tfw-update/SKILL.md из доверенного пакета 1.4 <точный путь, архив, URL или объект> к этому проекту 1.2 и выполни прямое обновление до 1.4`.",
        128: "3. До единственного Gate показываются service manifest, protected manifest и one-to-one карта legacy-source `work/<status>/<legacy-ID>/ → workspace/<legacy-ID>/`.",
        131: "6. В traces нормализуются только обязательные поля и живые пути `work/<status>/<ID>/ → workspace/<ID>/`; историческое описание остаётся provenance. Для `review`/`done` результат существует.",
        132: "7. Exact stock knowledge targets обновляются только при source-version hashes из принятой changelog map и совпавшем baseline.",
        153: "Публичный Assisted 1.4 был собран из принятой нейтральной 1.3 и проверенного change set. Он не содержит legacy TFW hook payload, `workspace/`, human profiles, персонализированную карточку, `knowledge/inbox/` или task evidence. Прямые маршруты проверяются на изолированных персонализированных фикстурах с manifests до/после; исходные releases остаются неизменными.",
        174: "- `AGENTS.md`, `README.md`, `MIGRATION.md`, пять skills, `team/README.md`, шаблон плана и active paths `workspace/`/`knowledge/` согласованы со stable-path моделью.",
        182: "2. **Manifest до записи:** фиксируются legacy-source `work/`/`people/`, `knowledge/` и их one-to-one targets `workspace/`/`team/` по относительному пути, размеру и SHA-256. Перед применением исходные хэши проверяются повторно.",
        183: "3. **One-to-one миграция задач:** каждый direct legacy-source task folder `work/<status>/<ID>/` переносится в `workspace/<ID>/` только если ID уникален, target отсутствует, `TRACE.md` существует, поле `ID задачи` совпадает с папкой, а поле `Статус` совпадает с исходным status-каталогом. ID и пользовательские артефакты не меняются.",
        184: "4. **Разрешённые изменения traces:** только нормализация обязательных полей без изменения смысла и замена живых путей `work/<status>/<ID>/` на `workspace/<ID>/` в поле `Результат` и актуальных ссылках. Историческое описание прежней схемы сохраняется и помечается как legacy. Для `review` и `done` итоговый результат существует.",
        185: "5. **Stock knowledge:** exact target заменяется версией назначения только при source-version SHA-256 из принятой changelog map. Изменённый пользователем файл считается конфликтом и не перезаписывается без отдельного решения.",
        186: "6. **Остальные защищённые материалы неизменны:** другие файлы `knowledge/`, все target-профили `team/` и пользовательские артефакты в `workspace/` совпадают по SHA-256, кроме отдельно показанных trace-изменений.",
        196: "- Проверка локальных файлов не доказывает завершение удалённой синхронизации выбранного провайдера.",
        222: "3. **Строки `Активная редакция: Assisted` и `Версия редакции: 1.0` в `PROJECT.md` сохраняются дословно.** Updater проверяет их как устойчивые markers совместимости; версия папки живёт отдельной строкой и в `VERSION`.",
        224: "5. **После обновления помощник отчитывается числами:** сколько файлов в `workspace/`, `knowledge/`, `team/` и сколько из них необъяснённо изменено — последнее число должно быть нулём.",
        228: "Полевое использование показало: помощник не всегда соблюдает порядок работы, если этого не потребовать явно. Просьба словами каждый раз звучит по-разному, и результат тоже разный. Команда — это записанная один раз просьба, которая выполняется одинаково.",
        234: "- Field overlay поверх TFW Assisted: заполненный проектный контекст, private knowledge и company identity оставались downstream; публичная производная сохраняет документ A4, заметку, план работы, презентацию и сборщик `build_a4.py` в нейтральном виде.",
        236: "Версия прошла полевое использование и стала behavioral source для публичной нейтральной производной.",
        242: "- Базовая редакция TFW Assisted: `AGENTS.md`, `README.md`, `PROJECT.md`, `MIGRATION.md`, `knowledge/INDEX.md`, `team/README.md` и prompt-only skills без shipped lifecycle runtime.",
    },
    "MIGRATION.md": {
        7: "Версия 1.6 поставляется только как целый нейтральный starter package с `VERSION=1.6`, exact versioned source object и dynamic observed manifest. Персонализированная папка, частичный service set или package с `workspace/`, human profiles, `project_id`, local bindings, task/pilot evidence, temp/conflict copies либо reparse points не является допустимым update source.",
        13: "`Используй /tfw-update и обнови этот проект из доверенного пакета 1.6 <точный путь, архив, URL или объект>`",
        18: "- protected manifest `workspace/`, `knowledge/`, `team/` и exact stock knowledge targets из version-specific карты;",
        20: "- source-version preconditions для exact stock knowledge targets либо отдельный точный records Gate для кастомизированного target; приватные имена и hashes не публикуются как общая норма;",
        21: "- доказательство, что package имеет `Состояние: НЕ ИНИЦИАЛИЗИРОВАН`, не содержит `project_id`, human profiles, `workspace/`, inbox, `.codex/`, identity helper или local state;",
        22: "- local-state exclusion: Full `bindings.yaml`, canonical Assisted `assisted/bindings.yml` и legacy `tfw-assisted/bindings.yml` не читаются из package/project root, не копируются, не изменяются и не входят ни в один manifest;",
        30: "4. Сохраните `workspace/`, `team/` и knowledge побайтово, кроме exact stock knowledge targets из принятой version-specific карты. При совпадении hash обновите только их; кастомизация без отдельного Gate останавливает запись.",
        34: "8. Докажите нулевой необъяснённый protected diff, только разрешённые knowledge changes, совпадение common active/package files кроме нейтрализованного `PROJECT.md`, package cleanliness и неизменность выбранного source object. Локальный post-read не является доказательством завершённой удалённой синхронизации.",
        40: "Версия 1.5 поставлялась как целый нейтральный starter package с `VERSION=1.5`. Персонализированная папка, marker candidate, частичный service set или пакет с legacy-source `work/`, human profiles, `project_id` и local bindings не являются допустимым update source.",
        46: "`Используй /tfw-update и обнови этот проект из доверенного пакета 1.5 <точный путь, архив, URL или объект>`",
        51: "- protected manifest legacy-source `work/`, `knowledge/`, `people/` и one-to-one targets `workspace/`, `team/`;",
        52: "- дословно сохраняемые карточку проекта, цели, knowledge, legacy task state при переносе `work/ → workspace/`, professional AI role и mental model;",
        54: "- local-state exclusion: Full `bindings.yaml`, canonical Assisted `assisted/bindings.yml` и legacy `tfw-assisted/bindings.yml` не читаются, не копируются и не входят в manifests;",
        63: "5. Не меняйте task IDs, владельцев, traces, результаты, общую карточку или knowledge, кроме exact stock knowledge targets из принятой source-version карты. Кастомизация требует отдельного решения; приватные имена и hashes не входят в общий договор.",
        64: "6. Не читайте и не копируйте local bindings из пакета, project root, Full `bindings.yaml`, canonical Assisted `assisted/bindings.yml` или legacy `tfw-assisted/bindings.yml`. Canonical Assisted entry создаётся на каждом устройстве отдельно после human gate.",
        77: "`Используй /tfw-update и обнови этот проект из доверенного пакета 1.4 <точный путь, архив, URL или объект>`",
        79: "Установленный prompt-only updater 1.3 получает целый пакет 1.4, статически читает changelog, показывает service manifest и version-specific protected migration, после чего ждёт одно согласование. Legacy-source `work/<legacy-ID>/` переносится one-to-one в `workspace/<legacy-ID>/`; карточка проекта, роли, ID, владельцы и результаты сохраняются.",
        85: "`Примени .agents/skills/tfw-update/SKILL.md из доверенного пакета 1.4 <точный путь, архив, URL или объект> к этому проекту 1.2 и выполни прямое обновление до 1.4`",
        87: "Локальный updater 1.2 запрещает изменения legacy-source `work/`, `knowledge/`, `people/`, поэтому не может быть договором полного прямого обновления. Договор берётся из целого проверенного пакета до Gate; код источника не исполняется.",
        89: "После одного согласования каждый legacy-source `work/<status>/<legacy-ID>/` переносится one-to-one в `workspace/<legacy-ID>/` только при уникальном ID, совпадающих полях ID/статуса, существующем trace и свободном target. Нормализуются только обязательные поля и живые пути; исторический текст, ID, владельцы и результаты не переписываются.",
        118: "2. Exact stock knowledge targets обновляются только при source-version hashes из `CHANGELOG.md`. Кастомизированный файл останавливает запись до отдельного решения.",
        119: "3. Все остальные существующие `knowledge/` сохраняются побайтово; legacy-source `work/` и `people/` сопоставляются one-to-one с `workspace/` и `team/`, кроме разрешённой нормализации legacy traces 1.2.",
        135: "2. Скопируйте туда исходные `README.md`, `AGENTS.md`, `TASKS.md`, весь `memory/`, legacy-source `work/` и отдельные результаты. Зафиксируйте дерево, размеры и SHA-256. Пока копия не проверена, ничего не заменяйте.",
        136: "3. Скопируйте служебную часть Assisted: `.agents/skills/`, `team/README.md`, `knowledge/INDEX.md`, корневые инструкции и шаблоны. Clean payload не добавляет `.codex/`; существующее unrelated содержимое этой папки не удаляется. Исходные `README.md` и `AGENTS.md` сохраняются в архиве.",
        138: "5. Для каждой строки исходного `TASKS.md` создайте отдельную стабильную папку `workspace/<ID>/`. ID не использует общий счётчик; исходный статус запишите в поле `Статус` внутри `TRACE.md`. Скопируйте trace и результаты без изменения смысла; при дальнейшей смене статуса папку не перемещайте.",
        151: "Релизы Assisted до 1.3 могли хранить задачу в legacy-source каталоге `work/<status>/<ID>/`. При миграции target становится `workspace/<ID>/`, статус живёт только в `TRACE.md`, а новый ID не содержит handle владельца. Уже существующие legacy-ID не переписываются.",
    },
    "knowledge/INDEX.md": {
        5: "- `records/` содержит проверенные долговечные записи проекта. Нейтральный starter не поставляет готовых фактов: записи появляются только из подтверждённой работы.",
        9: "## Что уже лежит в `records/`: пустое начальное состояние",
        10: "Проверенных записей пока нет; это ожидаемое состояние нового проекта.",
        11: "| Состояние | Что делать | Когда перепроверить |",
        12: "|:---|:---|:---|",
        13: "| Пусто | Не придумывать стартовые факты | Перед первой долговечной записью |",
        14: "| Новый кандидат | Сначала сохранить источник и автора | До переноса в `records/` |",
        15: "| Проверенная запись | Добавить её отдельным решением | При изменении предметной области |",
        16: "| Рискованный материал | Остановиться и запросить человеческое решение | До общей записи |",
        17: "Заполняйте `records/` только проверенными сведениями, которые действительно относятся к этому проекту.",
        18: "Нейтральный пакет не содержит предварительно заполненных фактов, людей, целей или организационных утверждений.",
    },
    "people/README.md": {
        3: "`team/` — общий каталог заявленных участников проекта, а не список того, кто сейчас находится за конкретным компьютером. Количество профилей не ограничено логикой TFW; агент обнаруживает их динамически.",
        7: "Один человек — один файл `team/<identifier>.md`. Имя файла содержит внутренний стабильный identifier из строчных латинских букв, цифр, `_` или `-`; `README.md` профилем не считается. Обычному человеку identifier и устройство хранения не показываются.",
        25: "Для автоматизации используйте отдельный файл `team/automation-<slug>.md` с `Идентификатор: automation:<slug>`, `Тип: automation`, обеими полями роли и отображаемым именем. Автоматизация не заимствует имя человека и не проходит human onboarding. Автономная task-роль handoff/review обычно вообще не требует отдельного профиля: она наследует владельца из trace и отмечает текущего участника как неприменимого.",
        39: "Assisted binding хранится в `%LOCALAPPDATA%\\tfw\\assisted\\bindings.yml` или `~/.tfw/assisted/bindings.yml` и не читает/не изменяет Full `bindings.yaml`. Оба local stores исключены из общей папки и package manifests; legacy `tfw-assisted/bindings.yml` сохраняется, но никогда не читается, не мигрирует и не служит fallback.",
    },
    "PROJECT.md": {
        12: "Нейтральный starter не знает этот проект. Заполните карточку, ценности, ограничения, аудиторию и признаки успеха из ответов пользователя; не переносите готовый пример как факт.",
        18: "| Название | НЕ УКАЗАНО — заполните при инициализации |",
        20: "| Для кого создаются результаты | НЕ УКАЗАНО — назовите реальную аудиторию проекта |",
        28: "Этот раздел не заполнен: рабочие ценности и принципы должны быть подтверждены для конкретного проекта.",
        29: "> Не оставляйте универсальные или демонстрационные формулировки вместо ответа пользователя.",
        30: "**Ценности проекта: НЕ УКАЗАНЫ.**",
        31: "Запишите только явно подтверждённые ценности и поясните, как каждая влияет на решения:",
        32: "- **Ценность 1:** НЕ УКАЗАНА.",
        33: "- **Ценность 2:** НЕ УКАЗАНА.",
        34: "- **Ценность 3:** НЕ УКАЗАНА.",
        35: "- **Ценность 4:** НЕ УКАЗАНА.",
        45: "Полезный результат в этом проекте определяется при инициализации и затем проверяется по его критериям:",
        49: "- он оформлен в согласованном для проекта виде, а не по вкусу модели;",
        56: "Профили людей и автоматизаций хранятся отдельными файлами в `team/` и обнаруживаются динамически; схема описана в `team/README.md`. При инициализации создаются только подтверждённые human-профили по полному имени с фамилией и двум ролям. Отсутствующая фамилия или коллизия требует уточнения; существующий профиль не перезаписывается.",
        58: "Общий проект не хранит «текущего пользователя». После инициализации выбор устройства лежит в `%LOCALAPPDATA%\\tfw\\assisted\\bindings.yml` на Windows или `~/.tfw/assisted/bindings.yml` на POSIX и адресуется стабильным `project_id`. Full `bindings.yaml` и legacy `tfw-assisted/bindings.yml` не читаются и не изменяются Assisted. Общий компьютер спрашивает участника в каждом новом человеческом чате.",
        64: "**Проектные ограничения: НЕ УКАЗАНЫ — заполните при инициализации.**",
        65: "Не переносите в этот раздел ограничения, факты или политику другого проекта.",
        66: "- **Хранилище и синхронизация:** укажите фактическую среду и правила shared writes.",
        67: "- **Чувствительные сведения:** определите, что нельзя сохранять в проекте или общей памяти.",
        68: "- **Проверенные сведения:** храните подтверждённые факты в `knowledge/records/` и обновляйте их отдельным решением.",
        69: "- **Высокорисковые решения:** назовите области, где ИИ не делает выводы или действия без специалиста.",
        70: "- **Внешние действия:** отправка, публикация, оплата и удаление требуют подтверждения человеком.",
    },
    "README.md": {
        5: "Это публичная нейтральная производная field-proven TFW Assisted 1.6. Starter не содержит персонализированную карточку, `project_id`, human profiles, `workspace/`, task evidence или machine-local bindings и после копирования готов к обычной инициализации.",
        16: "| Участники | `team/` |",
        17: "| Задачи, решения и проверки | `workspace/<ID>/TRACE.md` |",
        18: "| Проверенные сведения проекта | `knowledge/records/` |",
        31: "Device-local выбор Assisted хранится вне общей папки в `%LOCALAPPDATA%\\tfw\\assisted\\bindings.yml` на Windows или `~/.tfw/assisted/bindings.yml` на POSIX. Full `bindings.yaml` и legacy `tfw-assisted/bindings.yml` не читаются, не импортируются и не изменяются. Поэтому второй компьютер того же человека настраивается отдельно. Обычному участнику не нужно знать внутренние идентификаторы, форматы или команды.",
        37: "Путь задачи стабилен: `workspace/<ID>/`. Новые задачи используют `ID = YYYYMMDD-HHMMSS__slug` без login/handle; владелец всегда записан в поле `Владелец`. В новом slug запрещено `__`, а коллизия пути приводит к новому фактическому timestamp, а не к перезаписи. Legacy-ID `YYYYMMDD-HHMMSS__handle__slug` сохраняются при one-to-one миграции без изменения ID.",
        45: "3. создаёт отсутствующую `workspace/<ID>/`, устанавливает и проверяет `plan | <ID>`, затем создаёт `TRACE.md` и план по `шаблоны/план_работы.md`;",
        56: "Общие файлы проекта могут находиться в локальном или синхронизируемом shared-хранилище. Перед записью помощник перечитывает target и baseline, изменяет минимальный набор файлов и выполняет post-read/hash. Это помогает обнаружить конфликт, но не обещает безопасную параллельную запись или завершённую удалённую синхронизацию. Локальные bindings не входят в shared manifests.",
        83: "Обновление меняет служебную часть: `AGENTS.md`, `README.md`, `PROJECT.md`, `MIGRATION.md`, `VERSION`, `CHANGELOG.md`, `шаблоны/`, `.agents/skills/`. Папка `.codex/` не входит в clean payload. По умолчанию `workspace/`, `knowledge/` и `team/` защищены. Version-specific migration применяет только явные old-source → new-target карты; уже валидные identifiers сохраняются, а local bindings Full/Assisted и legacy registry никогда не читаются из пакета, не мигрируются и не переносятся между устройствами.",
        93: "| 1.5 | `Используй /tfw-update и обнови этот проект из доверенного пакета 1.6 <точный путь, архив, URL или объект>` | Пакет 1.6 содержит точную migration map, сохраняет project identity, персонализацию и valid identifiers, исключает local stores и добавляет prompt-only identity без обязательного helper |",
        96: "Каждый маршрут имеет один Gate записи. Для 1.5→1.6 помощник показывает service/protected manifests и source-version preconditions, сохраняет существующий валидный `project_id`, карточку, цели, роли, legacy-source `work/` как target `workspace/`, остальные knowledge и все valid profile filenames/identifiers как target `team/`. Stock knowledge targets обновляются только при exact hashes из `CHANGELOG.md` либо по отдельному точному records Gate; любой необъяснённый protected diff останавливает запись.",
        102: "1. до результата создать `workspace/<ID>/TRACE.md`;",
    },
    "шаблоны/build_a4.py": {
        2: '"""Сборка печатного A4-документа из Markdown по нейтральному стилю TFW Assisted.',
        12: "  --primary:#243B53; --blue:#334E68; --accent:#D9E2EC; --purple:#486581;",
        13: "  --text:#1F2933; --muted:#52606D; --line:#BCCCDC; --light:#F0F4F8;",
        30: "blockquote{margin:10px 0;padding:8px 14px;border-left:4px solid var(--accent);background:rgba(217,226,236,.55);font-style:normal}",
        135: "            parts.append('<div class=\"doc-head\"><img src=\"assets/tfw-mark.svg\" alt=\"TFW\">')",
    },
    "шаблоны/документ_A4.md": {
        2: "> Проект · для кого документ · автор · [дата] · редакция 1",
        94: "*Нейтральный шаблон служебного документа · собирается сборщиком `build_a4.py`*",
    },
    "шаблоны/заметка.md": {
        1: "# Переход на новый тариф в пилотном регионе",
        25: "- [[Встреча с партнёром 8 августа]]",
        43: "**Название заметки — это её содержание.** «Переход на новый тариф в пилотном регионе»",
    },
    "шаблоны/план_работы.md": {
        3: "> Заполните план в `workspace/<ID>/TRACE.md` от результата назад и согласуйте Gate 0 до активных изменений. Новый ID имеет вид `YYYYMMDD-HHMMSS__slug` без handle; legacy-ID и путь после создания не меняются. Сразу после создания папки plan устанавливает и проверяет `plan | <ID>`.",
        78: "**Gate 3:** `PASS` оставляет `review` до решения владельца приёмки; `FAIL` возвращает статус `doing` для нового handoff. В автономном режиме plan сам создаёт следующий этап только после обязательного отчёта и read-only сверки trace. Путь `workspace/<ID>/` не меняется.",
    },
    "шаблоны/презентация.html": {
        6: "<title>Шаблон презентации TFW Assisted</title>",
        9: "  НЕЙТРАЛЬНЫЙ ШАБЛОН ПРЕЗЕНТАЦИИ TFW ASSISTED",
        12: "  Что не трогать: всё, что между <style> и </style>. Это встроенный нейтральный вид:",
        30: "            --text-heading: #243B53;",
        35: "            --brand-primary: #243B53;",
        36: "            --brand-blue: #334E68;",
        37: "            --brand-highlight: #D9E2EC;",
        38: "            --brand-purple: #486581;",
        39: "            --info-bg: rgba(51, 78, 104, 0.10);",
        40: "            --info-border: #334E68;",
        41: "            --success-bg: rgba(217, 226, 236, 0.55);",
        42: "            --success-border: #486581;",
        43: "            --warning-bg: rgba(72, 101, 129, 0.12);",
        44: "            --warning-border: #486581;",
        114: "        .num-card.accent { background: rgba(217,226,236,0.65); border-color: var(--brand-highlight); }",
        153: "        .title-slide { background: linear-gradient(135deg, #243B53 0%, #486581 100%); color: #fff; justify-content: center; }",
        226: ".pause{background:linear-gradient(150deg,#102A43 0%,#243B53 58%,#334E68 100%);color:#fff}",
        264: ".pause .box-blue{background:rgba(51,78,104,.28) !important;border-color:#9FB3C8 !important}",
        265: ".pause .box-purple{background:rgba(72,101,129,.28) !important;border-color:#BCCCDC !important}",
        279: ".pause .box-blue{background:rgba(51,78,104,.30) !important;border-color:#9FB3C8 !important}",
        280: ".pause .box-purple{background:rgba(72,101,129,.30) !important;border-color:#BCCCDC !important}",
        289: "  <img src=\"assets/tfw-mark.svg\" class=\"logo\" alt=\"TFW\" style=\"filter:brightness(0) invert(1);opacity:.95;height:34px\">",
        294: "    <p style=\"font-size:17px;color:rgba(255,255,255,.9);margin:26px 0 0\">Имя Фамилия — роль в проекте</p>",
        296: "  <div class=\"foot\">[дата]</div>",
        302: "  <img src=\"assets/tfw-mark.svg\" class=\"logo\" alt=\"TFW\">",
        337: "  <img src=\"assets/tfw-mark.svg\" class=\"logo\" alt=\"TFW\">",
        362: "  <img src=\"assets/tfw-mark.svg\" class=\"logo\" alt=\"TFW\" style=\"filter:brightness(0) invert(1);opacity:.9\">",
        380: "          <li>Цвета и шрифт — это встроенный нейтральный вид</li>",
        381: "          <li>Файл <code>assets/tfw-mark.svg</code> рядом с шаблоном: это пассивный знак</li>",
    },
}


DELETE_BASELINES = {
    "шаблоны/overlay/theme.css": "69cc5a26887dc405c7ce5b289e72486643a1d2b0cfd83725d8296fcd8ebf3433",
    "шаблоны/theme.css": "6072dca48147ec02342b4de132677f11169ea3a870257c8b2b5351b5a5a12e2b",
    "../maintenance/maintenance-policy.json": "f044ec7925f663fa58dbe2fd0bce9ed86d9373633a7443993d5950683fe7e70f",
    "../maintenance/release-manifest.json": "57ef3be54dd6ca77ecef6e55658b9307493d507b4924b03543db5e94f9d405d7",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_bytes(relative: str) -> bytes:
    data = (SOURCE / Path(relative)).read_bytes()
    size, prefix = SOURCE_BASELINES[relative]
    if len(data) != size or not sha256(data).startswith(prefix):
        raise RuntimeError(f"source drift: {relative}")
    return data


def checked_product_path(relative: str) -> Path:
    path = (TARGET / Path(relative)).resolve(strict=False)
    editions = (REPO / "editions").resolve()
    if editions not in path.parents:
        raise RuntimeError(f"product path escaped editions/: {relative}")
    return path


def replace_source_lines(relative: str, replacements: dict[int, str]) -> bytes:
    source = source_bytes(relative)
    text = source.decode("utf-8")
    lines = text.splitlines(keepends=True)
    for number, replacement in sorted(replacements.items()):
        original = lines[number - 1]
        if original.endswith("\r\n"):
            ending = "\r\n"
        elif original.endswith("\n"):
            ending = "\n"
        elif original.endswith("\r"):
            ending = "\r"
        else:
            ending = ""
        original_body = original[: len(original) - len(ending)] if ending else original
        if replacement == original_body:
            raise RuntimeError(f"replacement is unchanged: {relative}:{number}")
        lines[number - 1] = replacement + ending
    return "".join(lines).encode("utf-8")


def git_text(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=REPO, text=True).strip()


def main() -> None:
    if git_text("branch", "--show-current") != EXPECTED_BRANCH:
        raise RuntimeError("wrong executor branch")
    dirty = git_text("status", "--porcelain")
    permitted_trace = f"?? workspace/2026/{TASK_ID}/evidence/"
    if dirty and dirty != permitted_trace:
        raise RuntimeError(f"unexpected worktree state before materialization: {dirty}")

    if set(REPLACEMENTS) != set(ADAPTED_TARGETS):
        raise RuntimeError("adapted file coverage differs from the frozen 17-file set")
    changed_source_lines = sum(len(lines) for lines in REPLACEMENTS.values())
    if changed_source_lines != 205:
        raise RuntimeError(f"replacement coverage is {changed_source_lines}, expected 205")

    for relative in SOURCE_BASELINES:
        source_bytes(relative)

    writes: dict[Path, bytes] = {}
    for source_relative, target_relative in EXACT.items():
        writes[checked_product_path(target_relative)] = source_bytes(source_relative)
    for source_relative, target_relative in ADAPTED_TARGETS.items():
        writes[checked_product_path(target_relative)] = replace_source_lines(
            source_relative, REPLACEMENTS[source_relative]
        )
    if len(writes) != 23:
        raise RuntimeError(f"field-derived write set is {len(writes)}, expected 23")

    for path, data in writes.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    old_people = checked_product_path("people/README.md")
    if not old_people.is_file():
        raise RuntimeError("relocation source disappeared")
    old_people.unlink()

    for relative, expected_hash in DELETE_BASELINES.items():
        path = checked_product_path(relative)
        data = path.read_bytes()
        if sha256(data) != expected_hash:
            raise RuntimeError(f"delete baseline drift: {relative}")
        path.unlink()

    print("MATERIALIZED=23 field-derived writes + 5 deletions")
    print("SOURCE_LINE_REPLACEMENTS=205")
    print("ROUTING_DOCS_PENDING=2")


if __name__ == "__main__":
    main()
