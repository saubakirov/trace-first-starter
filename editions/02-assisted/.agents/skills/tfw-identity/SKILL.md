---
name: tfw-identity
description: Внутренний fail-closed механизм профилей и локальной привязки Assisted; отделяет участника, роли, task owner и роль ИИ.
---

# /tfw-identity

Эта команда — внутренний механизм `AGENTS.md`. Не показывай обычному человеку identifier, YAML, путь store или название locality profile, если он не просит техническую диагностику.

## Инварианты

- Профиль и binding — заявленная атрибуция, не аутентификация и не полномочие.
- Человек, роль в организации, роль в проекте, task owner и роль ИИ — пять разных полей.
- Существующий валидный identifier не переименовывается. Новый строится из подтверждённой фамилии; коллизия останавливает запись до смыслового уточнения.
- Один профиль допускает явное one-profile rule. Во всех неоднозначных состояниях участник не угадывается.
- Persistent state использует только `tfw-assisted`; namespace Full не читается, не импортируется и не изменяется.
- `operational-local-v1` проверяется перед каждой persistent операцией. `unsafe`, `unknown`, stale, unsupported, shared/project/source root, link/reparse/mount ambiguity, ACL/probe error, corrupt registry или foreign live lock означают ноль persistent writes и session-only.
- Проверка известных provider roots не защищает от скрытого или злонамеренного same-user copying.

## Служебные команды

```text
python .agents/skills/tfw-identity/scripts/tfw_identity.py inspect --project-root ROOT
python .agents/skills/tfw-identity/scripts/tfw_identity.py status --project-root ROOT
python .agents/skills/tfw-identity/scripts/tfw_identity.py resolve --project-root ROOT --input TEXT
python .agents/skills/tfw-identity/scripts/tfw_identity.py profile-manifest --project-root ROOT
python .agents/skills/tfw-identity/scripts/tfw_identity.py create-profile --project-root ROOT --expected-manifest SHA256 --display-name NAME --surname SURNAME --organization-role ROLE --project-role ROLE
python .agents/skills/tfw-identity/scripts/tfw_identity.py set-fixed --project-root ROOT --participant ID --assert-local
python .agents/skills/tfw-identity/scripts/tfw_identity.py set-ask --project-root ROOT --assert-local
python .agents/skills/tfw-identity/scripts/tfw_identity.py self-test
```

`--store` и `--shared-root` предназначены для изолированных проверок или явно выбранного безопасного пути. `--assert-local` — ограниченное утверждение пользователя о личном несинхронизируемом устройстве; оно не отменяет механические проверки и само по себе не превращает `unsafe/unknown` в `proven`.

До lock/temp записи созданный `tfw-assisted` namespace получает private owner/ACL или Unix mode, затем заново включается в полный pinned component chain. Namespace substitution, permissive ACL или непрочитанный owner возвращают session-only и оставляют registry/lock/temp отсутствующими. Запись registry выполняется под live OS lock, через same-directory temporary, flush/fsync, replace, permission recheck и post-read. Возраст lock-файла не разрешает удалять или обходить чужую блокировку. Новый shared profile создаётся только после совпавшего profile manifest и свободного target, затем перечитывается.
