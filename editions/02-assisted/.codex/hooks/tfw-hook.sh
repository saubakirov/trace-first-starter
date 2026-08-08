#!/bin/sh

event=${1:-}
actor_arg=${2:-}
payload=
if [ "$event" != "BindActor" ]; then
    payload=$(cat)
fi
secret_pattern='(AKIA[0-9A-Z]{16}|ASIA[0-9A-Z]{16}|sk-[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|([Aa][Pp][Ii][ _-]?[Kk][Ee][Yy]|[Tt][Oo][Kk][Ee][Nn]|[Pp][Aa][Ss][Ss][Ww][Oo][Rr][Dd]|пароль)[[:space:]]*[:=][[:space:]]*[^[:space:]]{8,})'

json_string() {
    printf '%s' "$payload" | sed -n "s/.*\"$1\"[[:space:]]*:[[:space:]]*\"\([^\"]*\)\".*/\1/p" | sed -n '1p'
}

json_escape() {
    printf '%s' "$1" | sed 's/["\\]/\\&/g'
}

emit_problem() {
    message=$(json_escape "$1")
    if [ "$event" = "SessionStart" ]; then
        printf '{"systemMessage":"%s","hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"%s"}}' "$message" "$message"
    else
        printf '{"systemMessage":"%s"}' "$message"
    fi
    exit 0
}

root_hits=
root_count=0
directory=$(pwd -P)
while :; do
    project_file=$directory/PROJECT.md
    if [ -f "$project_file" ] &&
       grep -Eq '^Активная редакция:[[:space:]]*Assisted[[:space:]]*$' "$project_file" &&
       grep -Eq '^Версия редакции:[[:space:]]*1\.0[[:space:]]*$' "$project_file"; then
        root_hits=$directory
        root_count=$((root_count + 1))
    fi
    [ "$directory" = / ] && break
    directory=${directory%/*}
    [ -n "$directory" ] || directory=/
done

[ "$root_count" -eq 0 ] && emit_problem 'TFW Assisted: однозначный корень с маркерами Assisted / 1.0 не найден; запись отменена.'
[ "$root_count" -gt 1 ] && emit_problem 'TFW Assisted: найдено несколько активных корней Assisted; запись отменена.'
root=$root_hits

state_base=${XDG_STATE_HOME:-${HOME:-/tmp}/.local/state}
if command -v cksum >/dev/null 2>&1; then
    set -- $(printf '%s' "$root" | cksum)
    root_key=$1
else
    root_key=$(basename "$root" | tr -cd 'A-Za-z0-9_-')
fi
state_dir=$state_base/tfw-assisted/$root_key
mkdir -p "$state_dir" || emit_problem 'TFW Assisted: локальное состояние недоступно; запись отменена.'

profile_ids() {
    for profile in "$root"/people/*.md; do
        [ -f "$profile" ] || continue
        [ "$(basename "$profile")" = README.md ] && continue
        id=$(sed -n 's/^Идентификатор:[[:space:]]*\([^[:space:]]*\)[[:space:]]*$/\1/p' "$profile" | sed -n '1p')
        [ -n "$id" ] || id=$(basename "$profile" .md)
        printf '%s\n' "$id"
    done
}

if [ "$event" = "BindActor" ]; then
    if ! printf '%s' "$actor_arg" | grep -Eq '^([a-z0-9][a-z0-9_-]{1,40}|automation:[a-z0-9][a-z0-9_-]{1,40})$'; then
        printf '{"systemMessage":"TFW Assisted: недопустимый ID участника; локальная привязка не изменена."}'
        exit 0
    fi
    if [ "${actor_arg#automation:}" = "$actor_arg" ] && ! profile_ids | grep -Fxq "$actor_arg"; then
        printf '{"systemMessage":"TFW Assisted: профиль участника не найден; локальная привязка не изменена."}'
        exit 0
    fi
    printf '%s\n' "$actor_arg" > "$state_dir/actor.txt"
    printf '{"systemMessage":"TFW Assisted: участник привязан только на этом устройстве."}'
    exit 0
fi

if [ "$event" = "RiskCheck" ]; then
    if printf '%s' "$payload" | grep -Eq "$secret_pattern"; then
        write_risk='risk=hold; reason=deterministic-secret-pattern'
        stamp=$(date -u '+%Y%m%dT%H%M%SZ')
        printf 'event=RiskCheck\nutc=%s\nroot=%s\noutcome=%s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" "$root" "$write_risk" > "$state_dir/event-$stamp-RiskCheck-$$.log"
        printf '{"safe":false,"decision":"hold","reason":"Обнаружен формальный признак секрета; общая запись запрещена."}'
    else
        stamp=$(date -u '+%Y%m%dT%H%M%SZ')
        printf 'event=RiskCheck\nutc=%s\nroot=%s\noutcome=risk=pass; deterministic-only=true\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" "$root" > "$state_dir/event-$stamp-RiskCheck-$$.log"
        printf '{"safe":true,"decision":"pass","reason":"Формальных признаков секрета нет; смысловые категории должен проверить агент."}'
    fi
    exit 0
fi

profiles=$(profile_ids)
profile_count=$(printf '%s\n' "$profiles" | sed '/^$/d' | wc -l | tr -d ' ')
actor=none
if [ "$profile_count" -eq 1 ]; then
    actor=$(printf '%s\n' "$profiles" | sed -n '1p')
elif [ -f "$state_dir/actor.txt" ]; then
    bound=$(sed -n '1p' "$state_dir/actor.txt")
    if printf '%s\n' "$profiles" | grep -Fxq "$bound" || printf '%s' "$bound" | grep -Eq '^automation:[a-z0-9][a-z0-9_-]{1,40}$'; then
        actor=$bound
    fi
fi

active_traces() {
    [ "$actor" = none ] && return
    for task in "$root"/work/doing/*; do
        [ -d "$task" ] || continue
        trace=$task/TRACE.md
        [ -f "$trace" ] || continue
        grep -Eq "^Владелец:[[:space:]]*$actor[[:space:]]*$" "$trace" && printf '%s\n' "$trace"
    done
}

write_event_log() {
    session=$(json_string session_id); [ -n "$session" ] || session=no-session
    turn=$(json_string turn_id); [ -n "$turn" ] || turn=no-turn
    safe=$(printf '%s' "$session-$turn" | tr -c 'A-Za-z0-9_-' '_')
    stamp=$(date -u '+%Y%m%dT%H%M%SZ')
    log=$state_dir/event-$stamp-$event-$safe-$$.log
    {
        printf 'event=%s\n' "$event"
        printf 'utc=%s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
        printf 'root=%s\n' "$root"
        printf 'outcome=%s\n' "$1"
    } > "$log"
}

active=$(active_traces)
active_count=$(printf '%s\n' "$active" | sed '/^$/d' | wc -l | tr -d ' ')

if [ "$event" = "SessionStart" ]; then
    source=$(json_string source); [ -n "$source" ] || source=unknown
    counts=
    for status in new doing review done blocked; do
        count=0
        for task in "$root"/work/$status/*; do [ -d "$task" ] && count=$((count + 1)); done
        if [ -n "$counts" ]; then counts="$counts, $status=$count"; else counts="$status=$count"; fi
    done
    if [ "$active_count" -eq 1 ]; then
        active_name=$(basename "$(dirname "$active")")
    elif [ "$active_count" -gt 1 ]; then
        active_name=ambiguous
    else
        active_name=none
    fi
    summary="TFW Assisted активен ($source). Корень: $root; участник: $actor; active_task=$active_name; задачи $counts. До долговечной записи создайте trace."
    write_event_log "source=$source; actor=$actor; active=$active_name"
    escaped=$(json_escape "$summary")
    printf '{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"%s"}}' "$escaped"
    exit 0
fi

if [ "$event" = "PreCompact" ]; then
    trigger=$(json_string trigger); [ -n "$trigger" ] || trigger=unknown
    if [ "$active_count" -eq 1 ]; then
        trace=$active
        session=$(json_string session_id); [ -n "$session" ] || session=no-session
        turn=$(json_string turn_id); [ -n "$turn" ] || turn=no-turn
        marker="<!-- tfw:checkpoint:$session:$turn -->"
        if ! grep -Fq "$marker" "$trace"; then
            grep -Fq '## Checkpoints' "$trace" || printf '\n## Checkpoints\n' >> "$trace"
            {
                printf '\n%s\n' "$marker"
                printf -- '- UTC: %s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
                printf -- '- Причина: %s\n' "$trigger"
                printf -- '- Продолжение: перечитать цель, критерии и последнюю проверенную запись хода работы.\n'
            } >> "$trace"
            write_event_log "checkpoint=created; trace=$trace"
        else
            write_event_log "checkpoint=existing; trace=$trace"
        fi
    else
        write_event_log "checkpoint=none; active_count=$active_count"
    fi
    printf '{}'
    exit 0
fi

[ "$event" = "Stop" ] || emit_problem 'TFW Assisted: неизвестное событие; запись отменена.'

issues=
issue_count=0
add_issue() {
    issue_count=$((issue_count + 1))
    [ "$issue_count" -le 4 ] && issues=${issues:+$issues'; '}$1
}

for status in new doing review done blocked; do
    for task in "$root"/work/$status/*; do
        [ -d "$task" ] || continue
        relative=${task#"$root"/}
        trace=$task/TRACE.md
        if [ ! -f "$trace" ]; then
            add_issue "$relative: нет TRACE.md"
            continue
        fi
        task_name=$(basename "$task")
        if ! printf '%s' "$task_name" | grep -Eq '^[0-9]{8}-[0-9]{6}__[a-z0-9][a-z0-9_-]*__[a-z0-9][a-z0-9_-]*$' ||
           ! grep -Eq "^ID задачи:[[:space:]]*$task_name[[:space:]]*$" "$trace"; then
            add_issue "$relative: ID задачи не равен имени папки"
        fi
        missing=0
        for field in 'ID задачи' 'Владелец' 'Роль ИИ' 'Желаемый результат' 'Критерии' 'Результат' 'Решение о знании'; do
            grep -Eq "^$field:[[:space:]]*[^[:space:]]" "$trace" || missing=1
        done
        [ "$missing" -eq 1 ] && add_issue "$relative: неполный контракт trace"
        grep -Eq "^Статус:[[:space:]]*$status[[:space:]]*$" "$trace" || add_issue "$relative: статус в trace не равен папке $status"
        plan_line=$(grep -n -F '## План от результата назад' "$trace" | sed -n '1s/:.*//p')
        work_line=$(grep -n -F '## Ход работы' "$trace" | sed -n '1s/:.*//p')
        if [ -z "$plan_line" ] || [ -z "$work_line" ] || [ "$plan_line" -gt "$work_line" ]; then
            add_issue "$relative: обратный план отсутствует до хода работы"
        fi
        if [ "$status" = review ] || [ "$status" = done ]; then
            result=$(sed -n 's/^Результат:[[:space:]]*//p' "$trace" | sed -n '1p')
            if [ -z "$result" ] || [ "$result" = 'не создан' ]; then
                add_issue "$relative: результат не указан"
            elif [ ! -e "$root/$result" ]; then
                add_issue "$relative: путь результата не существует"
            fi
        fi
    done
done

for candidate in "$root"/knowledge/inbox/*.md; do
    [ -f "$candidate" ] || continue
    valid=1
    candidate_id=$(basename "$candidate" .md)
    if ! printf '%s' "$candidate_id" | grep -Eq '^[0-9]{8}-[0-9]{6}__[a-z0-9][a-z0-9_-]*__[a-z0-9][a-z0-9_-]*$'; then
        valid=0
    else
        grep -Eq "^ID кандидата:[[:space:]]*$candidate_id[[:space:]]*$" "$candidate" || valid=0
    fi
    grep -Eq '^ID кандидата:[[:space:]]*[^[:space:]]' "$candidate" || valid=0
    grep -Eq '^Источник:[[:space:]]*[^[:space:]]' "$candidate" || valid=0
    grep -Eq '^Автор:[[:space:]]*[^[:space:]]' "$candidate" || valid=0
    grep -Eq '^Проверка риска:[[:space:]]*пройдена[[:space:]]*$' "$candidate" || valid=0
    [ "$valid" -eq 1 ] || add_issue "knowledge/inbox/$(basename "$candidate"): кандидат не прошёл структурную проверку"
done

for area in "$root"/work "$root"/knowledge; do
    [ -d "$area" ] || continue
    find "$area" -type f -print | while IFS= read -r file; do
        if grep -Eq "$secret_pattern" "$file"; then
            printf '%s\n' "${file#"$root"/}"
        fi
    done > "$state_dir/secret-matches-$$.tmp"
    while IFS= read -r relative; do [ -n "$relative" ] && add_issue "$relative: обнаружен секретоподобный материал"; done < "$state_dir/secret-matches-$$.tmp"
    rm -f "$state_dir/secret-matches-$$.tmp"
done

if [ "$issue_count" -gt 0 ]; then
    [ "$issue_count" -gt 4 ] && issues="$issues; и ещё $((issue_count - 4))"
    if printf '%s' "$payload" | grep -Eq '"stop_hook_active"[[:space:]]*:[[:space:]]*true'; then
        write_event_log "mismatch=$issues; continued=true"
        escaped=$(json_escape "TFW Assisted: рассогласование осталось после одного продолжения — $issues. Цикл остановлен; сообщите пользователю.")
        printf '{"systemMessage":"%s"}' "$escaped"
    else
        write_event_log "mismatch=$issues; continued=false"
        escaped=$(json_escape "TFW Assisted: одно продолжение для сверки — $issues. Исправьте только безопасное и однозначное, иначе сообщите пользователю.")
        printf '{"decision":"block","reason":"%s"}' "$escaped"
    fi
    exit 0
fi

write_event_log aligned
printf '{}'
