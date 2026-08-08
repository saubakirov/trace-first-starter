param(
    [Parameter(Mandatory = $true)][string]$Event,
    [string]$ActorId = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
$script:SecretPattern = '(?i)(AKIA[0-9A-Z]{16}|ASIA[0-9A-Z]{16}|sk-[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|(?:api[_ -]?key|token|password|пароль)\s*[:=]\s*\S{8,})'

function Emit-Json([hashtable]$Value) {
    [Console]::Out.Write(($Value | ConvertTo-Json -Depth 6 -Compress))
    exit 0
}

function Get-InputValue([string]$Name, $Default = "") {
    $property = $script:Payload.PSObject.Properties[$Name]
    if ($null -eq $property -or $null -eq $property.Value) { return $Default }
    return $property.Value
}

function Find-AssistedRoot {
    $matches = @()
    $directory = [System.IO.DirectoryInfo](Get-Location).Path
    while ($null -ne $directory) {
        $projectFile = Join-Path $directory.FullName "PROJECT.md"
        if (Test-Path -LiteralPath $projectFile -PathType Leaf) {
            $text = Get-Content -LiteralPath $projectFile -Raw -Encoding UTF8
            $edition = [regex]::IsMatch($text, '(?m)^Активная редакция:\s*Assisted\s*$')
            $version = [regex]::IsMatch($text, '(?m)^Версия редакции:\s*1\.0\s*$')
            if ($edition -and $version) { $matches += $directory.FullName }
        }
        $directory = $directory.Parent
    }
    if ($matches.Count -eq 1) {
        return [pscustomobject]@{ Root = $matches[0]; Error = "" }
    }
    if ($matches.Count -eq 0) {
        return [pscustomobject]@{ Root = ""; Error = "TFW Assisted: однозначный корень с маркерами Assisted / 1.0 не найден; запись отменена." }
    }
    return [pscustomobject]@{ Root = ""; Error = "TFW Assisted: найдено несколько активных корней Assisted; запись отменена." }
}

function Emit-Problem([string]$Message) {
    if ($Event -eq "SessionStart") {
        Emit-Json @{
            systemMessage = $Message
            hookSpecificOutput = @{
                hookEventName = "SessionStart"
                additionalContext = $Message
            }
        }
    }
    Emit-Json @{ systemMessage = $Message }
}

function Get-StateDirectory([string]$Root) {
    $base = if ([string]::IsNullOrWhiteSpace($env:LOCALAPPDATA)) {
        Join-Path ([System.IO.Path]::GetTempPath()) "TFW-Assisted"
    } else {
        Join-Path $env:LOCALAPPDATA "TFW-Assisted"
    }
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        $bytes = [System.Text.Encoding]::UTF8.GetBytes($Root.ToLowerInvariant())
        $hash = $sha.ComputeHash($bytes)
    } finally {
        $sha.Dispose()
    }
    $key = (($hash[0..7] | ForEach-Object { $_.ToString("x2") }) -join "")
    $path = Join-Path $base $key
    New-Item -ItemType Directory -Path $path -Force | Out-Null
    return $path
}

function Get-ProfileIds([string]$Root) {
    $people = Join-Path $Root "people"
    if (-not (Test-Path -LiteralPath $people -PathType Container)) { return @() }
    $ids = @()
    foreach ($file in @(Get-ChildItem -LiteralPath $people -File -Filter "*.md" | Where-Object Name -ne "README.md")) {
        $text = Get-Content -LiteralPath $file.FullName -Raw -Encoding UTF8
        $match = [regex]::Match($text, '(?m)^Идентификатор:\s*(\S+)\s*$')
        $ids += if ($match.Success) { $match.Groups[1].Value } else { $file.BaseName }
    }
    return @($ids)
}

function Get-Actor([string]$Root, [string]$StateDirectory) {
    $ids = @(Get-ProfileIds $Root)
    if ($ids.Count -eq 1) { return $ids[0] }
    $bindingFile = Join-Path $StateDirectory "actor.txt"
    if (Test-Path -LiteralPath $bindingFile -PathType Leaf) {
        $bound = (Get-Content -LiteralPath $bindingFile -Raw -Encoding UTF8).Trim()
        if ($ids -contains $bound -or $bound -match '^automation:[a-z0-9][a-z0-9_-]{1,40}$') { return $bound }
    }
    return "none"
}

function Get-ActiveTraces([string]$Root, [string]$Actor) {
    if ($Actor -eq "none") { return @() }
    $doing = Join-Path $Root "work\doing"
    if (-not (Test-Path -LiteralPath $doing -PathType Container)) { return @() }
    $traces = @()
    foreach ($task in @(Get-ChildItem -LiteralPath $doing -Directory)) {
        $trace = Join-Path $task.FullName "TRACE.md"
        if (-not (Test-Path -LiteralPath $trace -PathType Leaf)) { continue }
        $text = Get-Content -LiteralPath $trace -Raw -Encoding UTF8
        $owner = [regex]::Match($text, '(?m)^Владелец:\s*(\S+)\s*$')
        if ($owner.Success -and $owner.Groups[1].Value -eq $Actor) { $traces += $trace }
    }
    return @($traces)
}

function Write-EventLog([string]$StateDirectory, [string]$Outcome) {
    $session = [string](Get-InputValue "session_id" "no-session")
    $turn = [string](Get-InputValue "turn_id" "no-turn")
    $safe = (($session + "-" + $turn) -replace '[^A-Za-z0-9_-]', '_')
    $stamp = [DateTime]::UtcNow.ToString("yyyyMMddTHHmmssfffZ")
    $log = Join-Path $StateDirectory ("event-{0}-{1}-{2}.log" -f $stamp, $Event, $safe)
    $lines = @(
        "event=$Event",
        "utc=$([DateTime]::UtcNow.ToString('o'))",
        "root=$Root",
        "outcome=$Outcome"
    )
    Set-Content -LiteralPath $log -Value $lines -Encoding UTF8
}

$script:Payload = [pscustomobject]@{}
if ($Event -ne "BindActor") {
    $raw = [Console]::In.ReadToEnd()
    if (-not [string]::IsNullOrWhiteSpace($raw)) {
        try { $script:Payload = $raw | ConvertFrom-Json }
        catch { Emit-Problem "TFW Assisted: вход события не прочитан; запись отменена." }
    }
}

$rootResult = Find-AssistedRoot
if (-not [string]::IsNullOrWhiteSpace($rootResult.Error)) { Emit-Problem $rootResult.Error }
$Root = $rootResult.Root
$stateDirectory = Get-StateDirectory $Root

if ($Event -eq "BindActor") {
    if ($ActorId -notmatch '^[a-z0-9][a-z0-9_-]{1,40}$' -and $ActorId -notmatch '^automation:[a-z0-9][a-z0-9_-]{1,40}$') {
        Emit-Json @{ systemMessage = "TFW Assisted: недопустимый ID участника; локальная привязка не изменена." }
    }
    $profiles = @(Get-ProfileIds $Root)
    if (-not ($profiles -contains $ActorId) -and $ActorId -notmatch '^automation:') {
        Emit-Json @{ systemMessage = "TFW Assisted: профиль участника не найден; локальная привязка не изменена." }
    }
    Set-Content -LiteralPath (Join-Path $stateDirectory "actor.txt") -Value $ActorId -Encoding UTF8
    Emit-Json @{ systemMessage = "TFW Assisted: участник привязан только на этом устройстве." }
}

if ($Event -eq "RiskCheck") {
    $material = [string](Get-InputValue "material" "")
    if ([regex]::IsMatch($material, $script:SecretPattern)) {
        Write-EventLog $stateDirectory "risk=hold; reason=deterministic-secret-pattern"
        Emit-Json @{ safe = $false; decision = "hold"; reason = "Обнаружен формальный признак секрета; общая запись запрещена." }
    }
    Write-EventLog $stateDirectory "risk=pass; deterministic-only=true"
    Emit-Json @{ safe = $true; decision = "pass"; reason = "Формальных признаков секрета нет; смысловые категории должен проверить агент." }
}

$actor = Get-Actor $Root $stateDirectory
$activeTraces = @(Get-ActiveTraces $Root $actor)

if ($Event -eq "SessionStart") {
    $source = [string](Get-InputValue "source" "unknown")
    $counts = @{}
    foreach ($status in @("new", "doing", "review", "done", "blocked")) {
        $path = Join-Path $Root ("work\" + $status)
        $counts[$status] = if (Test-Path -LiteralPath $path -PathType Container) {
            @(Get-ChildItem -LiteralPath $path -Directory).Count
        } else { 0 }
    }
    $active = if ($activeTraces.Count -eq 1) {
        Split-Path (Split-Path $activeTraces[0] -Parent) -Leaf
    } elseif ($activeTraces.Count -gt 1) { "ambiguous" } else { "none" }
    $summary = "TFW Assisted активен ($source). Корень: $Root; участник: $actor; active_task=$active; задачи new=$($counts.new), doing=$($counts.doing), review=$($counts.review), done=$($counts.done), blocked=$($counts.blocked). До долговечной записи создайте trace."
    Write-EventLog $stateDirectory ("source=" + $source + "; actor=" + $actor + "; active=" + $active)
    Emit-Json @{ hookSpecificOutput = @{ hookEventName = "SessionStart"; additionalContext = $summary } }
}

if ($Event -eq "PreCompact") {
    $trigger = [string](Get-InputValue "trigger" "unknown")
    if ($activeTraces.Count -eq 1) {
        $trace = $activeTraces[0]
        $session = [string](Get-InputValue "session_id" "no-session")
        $turn = [string](Get-InputValue "turn_id" "no-turn")
        $marker = "<!-- tfw:checkpoint:$session`:$turn -->"
        $text = Get-Content -LiteralPath $trace -Raw -Encoding UTF8
        if (-not $text.Contains($marker)) {
            if (-not $text.Contains("## Checkpoints")) {
                Add-Content -LiteralPath $trace -Value "`n## Checkpoints" -Encoding UTF8
            }
            $entry = "`n$marker`n- UTC: $([DateTime]::UtcNow.ToString('o'))`n- Причина: $trigger`n- Продолжение: перечитать цель, критерии и последнюю проверенную запись хода работы."
            Add-Content -LiteralPath $trace -Value $entry -Encoding UTF8
            Write-EventLog $stateDirectory ("checkpoint=created; trace=" + $trace)
        } else {
            Write-EventLog $stateDirectory ("checkpoint=existing; trace=" + $trace)
        }
    } else {
        Write-EventLog $stateDirectory ("checkpoint=none; active_count=" + $activeTraces.Count)
    }
    Emit-Json @{}
}

if ($Event -ne "Stop") { Emit-Problem "TFW Assisted: неизвестное событие; запись отменена." }

$issues = [System.Collections.Generic.List[string]]::new()
$statuses = @("new", "doing", "review", "done", "blocked")
foreach ($status in $statuses) {
    $statusPath = Join-Path $Root ("work\" + $status)
    if (-not (Test-Path -LiteralPath $statusPath -PathType Container)) { continue }
    foreach ($task in @(Get-ChildItem -LiteralPath $statusPath -Directory)) {
        $trace = Join-Path $task.FullName "TRACE.md"
        $relativeTask = $task.FullName.Substring($Root.Length).TrimStart('\', '/')
        if (-not (Test-Path -LiteralPath $trace -PathType Leaf)) {
            $issues.Add("${relativeTask}: нет TRACE.md")
            continue
        }
        $text = Get-Content -LiteralPath $trace -Raw -Encoding UTF8
        if ($task.Name -notmatch '^\d{8}-\d{6}__[a-z0-9][a-z0-9_-]*__[a-z0-9][a-z0-9_-]*$' -or
            -not [regex]::IsMatch($text, "(?m)^ID задачи:\s*$([regex]::Escape($task.Name))\s*$")) {
            $issues.Add("${relativeTask}: ID задачи не равен имени папки")
        }
        foreach ($pattern in @(
            '(?m)^ID задачи:\s*\S+',
            '(?m)^Владелец:\s*\S+',
            '(?m)^Роль ИИ:\s*\S+',
            '(?m)^Желаемый результат:\s*\S+',
            '(?m)^Критерии:\s*\S+',
            '(?m)^Результат:\s*\S+',
            '(?m)^Решение о знании:\s*\S+'
        )) {
            if (-not [regex]::IsMatch($text, $pattern)) { $issues.Add("${relativeTask}: неполный контракт trace"); break }
        }
        if (-not [regex]::IsMatch($text, "(?m)^Статус:\s*$status\s*$")) {
            $issues.Add("${relativeTask}: статус в trace не равен папке $status")
        }
        $planAt = $text.IndexOf("## План от результата назад", [StringComparison]::Ordinal)
        $workAt = $text.IndexOf("## Ход работы", [StringComparison]::Ordinal)
        if ($planAt -lt 0 -or $workAt -lt 0 -or $planAt -gt $workAt) {
            $issues.Add("${relativeTask}: обратный план отсутствует до хода работы")
        }
        if ($status -in @("review", "done")) {
            $result = [regex]::Match($text, '(?m)^Результат:\s*(.+?)\s*$')
            if (-not $result.Success -or $result.Groups[1].Value -eq "не создан") {
                $issues.Add("${relativeTask}: результат не указан")
            } else {
                $resultPath = Join-Path $Root ($result.Groups[1].Value -replace '/', [IO.Path]::DirectorySeparatorChar)
                if (-not (Test-Path -LiteralPath $resultPath)) { $issues.Add("${relativeTask}: путь результата не существует") }
            }
        }
    }
}

$inbox = Join-Path $Root "knowledge\inbox"
if (Test-Path -LiteralPath $inbox -PathType Container) {
    foreach ($candidate in @(Get-ChildItem -LiteralPath $inbox -File -Filter "*.md")) {
        $text = Get-Content -LiteralPath $candidate.FullName -Raw -Encoding UTF8
        if ($candidate.BaseName -notmatch '^\d{8}-\d{6}__[a-z0-9][a-z0-9_-]*__[a-z0-9][a-z0-9_-]*$' -or
            -not [regex]::IsMatch($text, "(?m)^ID кандидата:\s*$([regex]::Escape($candidate.BaseName))\s*$")) {
            $issues.Add("knowledge/inbox/$($candidate.Name): ID кандидата не равен имени файла")
        }
        foreach ($pattern in @(
            '(?m)^ID кандидата:\s*\S+',
            '(?m)^Источник:\s*\S+',
            '(?m)^Автор:\s*\S+',
            '(?m)^Проверка риска:\s*пройдена\s*$'
        )) {
            if (-not [regex]::IsMatch($text, $pattern)) { $issues.Add("knowledge/inbox/$($candidate.Name): кандидат не прошёл структурную проверку"); break }
        }
    }
}

foreach ($area in @("work", "knowledge")) {
    $path = Join-Path $Root $area
    if (-not (Test-Path -LiteralPath $path -PathType Container)) { continue }
    foreach ($file in @(Get-ChildItem -LiteralPath $path -File -Recurse)) {
        $text = Get-Content -LiteralPath $file.FullName -Raw -Encoding UTF8
        if ([regex]::IsMatch($text, $script:SecretPattern)) {
            $relative = $file.FullName.Substring($Root.Length).TrimStart('\', '/')
            $issues.Add("${relative}: обнаружен секретоподобный материал")
        }
    }
}

if ($issues.Count -gt 0) {
    $summary = (@($issues | Select-Object -First 4) -join "; ")
    if ($issues.Count -gt 4) { $summary += "; и ещё $($issues.Count - 4)" }
    $alreadyContinued = (Get-InputValue "stop_hook_active" $false) -eq $true
    Write-EventLog $stateDirectory ("mismatch=" + $summary + "; continued=" + $alreadyContinued)
    if (-not $alreadyContinued) {
        Emit-Json @{ decision = "block"; reason = "TFW Assisted: одно продолжение для сверки — $summary. Исправьте только безопасное и однозначное, иначе сообщите пользователю." }
    }
    Emit-Json @{ systemMessage = "TFW Assisted: рассогласование осталось после одного продолжения — $summary. Цикл остановлен; сообщите пользователю." }
}

Write-EventLog $stateDirectory "aligned"
Emit-Json @{}
