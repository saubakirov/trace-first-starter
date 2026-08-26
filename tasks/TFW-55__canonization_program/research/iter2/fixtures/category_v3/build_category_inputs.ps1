param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('critic-packets', 'scorer-input')]
    [string]$Mode,

    [ValidateSet('Q7', 'M2', 'R5', 'K8', 'V1')]
    [string]$Label,

    [string]$RawOutputPath,

    [string]$ScorerOutputPath
)

$ErrorActionPreference = 'Stop'

$packageDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$fixturesDir = Split-Path -Parent $packageDir
$v2Path = Join-Path $fixturesDir 'frozen_design.v2.json'
$expectedV2Hash = 'd7fdb413af669abdf92cb3c055f7a966db3d4daec58d2ac15c36e679805f0f7a'
$actualV2Hash = (Get-FileHash -LiteralPath $v2Path -Algorithm SHA256).Hash.ToLowerInvariant()
if ($actualV2Hash -ne $expectedV2Hash) {
    throw "Frozen v2 hash mismatch: $actualV2Hash"
}

$design = Get-Content -LiteralPath $v2Path -Raw | ConvertFrom-Json
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$separator = "`n`n"

function ConvertTo-FrozenJson {
    param([Parameter(Mandatory = $true)]$Value)
    return ($Value | ConvertTo-Json -Depth 100 -Compress)
}

function Write-ExactUtf8 {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][string]$Text
    )
    $parent = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Path $parent -Force | Out-Null
    }
    [System.IO.File]::WriteAllText($Path, $Text, $utf8NoBom)
}

function Get-CategoryPacket {
    param([Parameter(Mandatory = $true)][string]$OpaqueLabel)

    $internalId = $design.randomization.category_mapping.$OpaqueLabel
    $variant = $design.category_family.variants | Where-Object { $_.id -eq $internalId }
    if ($null -eq $variant) {
        throw "No category variant for opaque label $OpaqueLabel"
    }

    $segments = @(
        [string]$design.common_prompt.system,
        [string]$design.common_prompt.category_task,
        (ConvertTo-FrozenJson $design.category_family.critic_output_schema),
        "VARIANT $OpaqueLabel",
        [string]$variant.packet,
        (ConvertTo-FrozenJson $design.category_family.neutral_cases)
    )
    return ($segments -join $separator)
}

function Get-ExactPropertyNames {
    param([Parameter(Mandatory = $true)]$Object)
    return @($Object.PSObject.Properties.Name | Sort-Object)
}

function Test-ExactProperties {
    param(
        [Parameter(Mandatory = $true)]$Object,
        [Parameter(Mandatory = $true)][string[]]$Expected
    )
    $actual = Get-ExactPropertyNames $Object
    $wanted = @($Expected | Sort-Object)
    return (($actual.Count -eq $wanted.Count) -and (-not (Compare-Object $actual $wanted)))
}

function Get-ProgrammaticChecks {
    param(
        [Parameter(Mandatory = $true)][string]$OpaqueLabel,
        [Parameter(Mandatory = $true)][string]$Packet,
        [Parameter(Mandatory = $true)][string]$RawOutput
    )

    $jsonParse = $false
    $rootExact = $false
    $caseFieldsExact = $false
    $labelMatch = $false
    $caseIdsExact = $false
    $caseCount = 0
    $legalEnums = $false
    $parsed = $null

    try {
        $parsed = $RawOutput | ConvertFrom-Json
        $jsonParse = $true
        $rootExact = Test-ExactProperties $parsed @(
            'variant_label', 'cases', 'definition', 'exclusions',
            'primary_category_claim', 'ambiguities', 'required_source_ids'
        )
        $labelMatch = ([string]$parsed.variant_label -eq $OpaqueLabel)
        $caseCount = @($parsed.cases).Count
        $caseFieldsExact = (@($parsed.cases | Where-Object {
            -not (Test-ExactProperties $_ @('case_id', 'classification', 'reason', 'when_apply'))
        }).Count -eq 0)
        $actualIds = @($parsed.cases | ForEach-Object { [string]$_.case_id })
        $expectedIds = @('N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7')
        $caseIdsExact = (($actualIds.Count -eq 7) -and (-not (Compare-Object $actualIds $expectedIds -SyncWindow 0)))
        $legalValues = @('TFW', 'NOT_TFW', 'INSUFFICIENT')
        $legalEnums = (@($parsed.cases | Where-Object { $legalValues -notcontains [string]$_.classification }).Count -eq 0)
    }
    catch {
        $parsed = $null
    }

    $schemaValid = $jsonParse -and $rootExact -and $caseFieldsExact -and $labelMatch -and $caseIdsExact -and ($caseCount -eq 7) -and $legalEnums
    return [ordered]@{
        json_parse = $jsonParse
        schema_valid = $schemaValid
        variant_label_match = $labelMatch
        case_ids_exact = $caseIdsExact
        case_count = $caseCount
        legal_enums = $legalEnums
        no_additional_properties = ($rootExact -and $caseFieldsExact)
        packet_utf8_bytes = $utf8NoBom.GetByteCount($Packet)
        packet_whitespace_words = @(($Packet -split '\s+') | Where-Object { $_ }).Count
        delivered_source_units = 1
    }
}

$frozenOrder = @($design.randomization.category_order)

if ($Mode -eq 'critic-packets') {
    $manifest = [ordered]@{
        package = 'TFW55-I2-CATEGORY-EXEC-v3'
        v2_sha256 = $actualV2Hash
        order = $frozenOrder
        packets = [ordered]@{}
    }
    foreach ($opaqueLabel in $frozenOrder) {
        $packet = Get-CategoryPacket $opaqueLabel
        $packetPath = Join-Path $packageDir "packets/critic_$opaqueLabel.txt"
        Write-ExactUtf8 $packetPath $packet
        $manifest.packets[$opaqueLabel] = [ordered]@{
            file = "packets/critic_$opaqueLabel.txt"
            sha256 = (Get-FileHash -LiteralPath $packetPath -Algorithm SHA256).Hash.ToLowerInvariant()
            utf8_bytes = $utf8NoBom.GetByteCount($packet)
            whitespace_words = @(($packet -split '\s+') | Where-Object { $_ }).Count
        }
    }
    $manifestPath = Join-Path $packageDir 'packet_manifest.generated.json'
    Write-ExactUtf8 $manifestPath (ConvertTo-FrozenJson $manifest)
    Write-Output (ConvertTo-FrozenJson $manifest)
    exit 0
}

if ([string]::IsNullOrWhiteSpace($Label) -or [string]::IsNullOrWhiteSpace($RawOutputPath) -or [string]::IsNullOrWhiteSpace($ScorerOutputPath)) {
    throw 'scorer-input requires -Label, -RawOutputPath, and -ScorerOutputPath'
}

$packetPath = Join-Path $packageDir "packets/critic_$Label.txt"
if (-not (Test-Path -LiteralPath $packetPath)) {
    throw "Missing preassembled critic packet: $packetPath"
}
$packet = [System.IO.File]::ReadAllText($packetPath, $utf8NoBom)
$rawOutput = [System.IO.File]::ReadAllText((Resolve-Path -LiteralPath $RawOutputPath), $utf8NoBom)
$checks = Get-ProgrammaticChecks -OpaqueLabel $Label -Packet $packet -RawOutput $rawOutput

$scorerSegments = @(
    [string]$design.scoring_protocol.scorer_system,
    ("PACKET`n" + $packet),
    ("RAW_OUTPUT`n" + $rawOutput),
    ("PROGRAMMATIC_CHECKS`n" + (ConvertTo-FrozenJson $checks)),
    ("EXPECTED`n" + (ConvertTo-FrozenJson $design.category_family.answer_key_under_provisional_fixture)),
    ("RUBRIC`n" + (ConvertTo-FrozenJson $design.rubric)),
    ("OUTPUT_SCHEMA`n" + (ConvertTo-FrozenJson $design.scoring_protocol.scorer_output_schemas.category))
)
$scorerInput = $scorerSegments -join $separator
Write-ExactUtf8 $ScorerOutputPath $scorerInput

$result = [ordered]@{
    package = 'TFW55-I2-CATEGORY-EXEC-v3'
    opaque_label = $Label
    critic_packet_sha256 = (Get-FileHash -LiteralPath $packetPath -Algorithm SHA256).Hash.ToLowerInvariant()
    raw_output_sha256 = (Get-FileHash -LiteralPath (Resolve-Path -LiteralPath $RawOutputPath) -Algorithm SHA256).Hash.ToLowerInvariant()
    scorer_input_sha256 = (Get-FileHash -LiteralPath $ScorerOutputPath -Algorithm SHA256).Hash.ToLowerInvariant()
    scorer_input_utf8_bytes = $utf8NoBom.GetByteCount($scorerInput)
    programmatic_checks = $checks
}
Write-Output (ConvertTo-FrozenJson $result)
