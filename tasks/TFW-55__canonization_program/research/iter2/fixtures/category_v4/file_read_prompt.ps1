param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('critic', 'scorer')]
    [string]$Role,

    [Parameter(Mandatory = $true)]
    [string]$InputPath,

    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[0-9a-fA-F]{64}$')]
    [string]$ExpectedInputSha256,

    [Parameter(Mandatory = $true)]
    [string]$AttestationPath
)

$ErrorActionPreference = 'Stop'

$packageDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$fixturesDir = Split-Path -Parent $packageDir
$iter2Dir = Split-Path -Parent $fixturesDir
$v2Path = Join-Path $fixturesDir 'frozen_design.v2.json'
$v3Dir = Join-Path $fixturesDir 'category_v3'
$v3DesignPath = Join-Path $v3Dir 'category_execution.v3.json'
$v3SumsPath = Join-Path $v3Dir 'SHA256SUMS'
$challengeRunRoot = Join-Path $iter2Dir 'challenge_runs/category_v4'

$expectedV2Hash = 'd7fdb413af669abdf92cb3c055f7a966db3d4daec58d2ac15c36e679805f0f7a'
$expectedV3DesignHash = '8e53b00a305dde62f1697015daf3ece76fdca3351714ce48fda0f642a09d3500'
$expectedV3SumsHash = '72abfa80de41a0427ddd4577235bd3e08df8072cde93d187002842fab49f4ee6'

function Get-LowerSha256 {
    param([Parameter(Mandatory = $true)][string]$Path)
    return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
}

function Assert-Hash {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][string]$Expected
    )
    $actual = Get-LowerSha256 $Path
    if ($actual -ne $Expected.ToLowerInvariant()) {
        throw "SHA-256 mismatch for $Path`: expected $Expected, actual $actual"
    }
    return $actual
}

function Assert-PathWithin {
    param(
        [Parameter(Mandatory = $true)][string]$Candidate,
        [Parameter(Mandatory = $true)][string]$AllowedRoot
    )
    $rootFull = [System.IO.Path]::GetFullPath($AllowedRoot).TrimEnd([System.IO.Path]::DirectorySeparatorChar) + [System.IO.Path]::DirectorySeparatorChar
    $candidateFull = [System.IO.Path]::GetFullPath($Candidate)
    if (-not $candidateFull.StartsWith($rootFull, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Path is outside allowed root: $candidateFull"
    }
    return $candidateFull
}

$v2Hash = Assert-Hash -Path $v2Path -Expected $expectedV2Hash
$v3DesignHash = Assert-Hash -Path $v3DesignPath -Expected $expectedV3DesignHash
$v3SumsHash = Assert-Hash -Path $v3SumsPath -Expected $expectedV3SumsHash

$v3Failures = @()
Get-Content -LiteralPath $v3SumsPath | ForEach-Object {
    if ($_ -notmatch '^([0-9a-f]{64})  (.+)$') {
        $v3Failures += "malformed: $_"
        return
    }
    $entryPath = Join-Path $v3Dir $Matches[2]
    $actual = Get-LowerSha256 $entryPath
    if ($actual -ne $Matches[1]) {
        $v3Failures += "$($Matches[2]):$actual"
    }
}
if ($v3Failures.Count -gt 0) {
    throw "category_v3 SHA256SUMS verification failed: $($v3Failures -join ', ')"
}

$resolvedInput = (Resolve-Path -LiteralPath $InputPath).Path
if ($Role -eq 'critic') {
    $allowedCriticRoot = Join-Path $v3Dir 'packets'
    $resolvedInput = Assert-PathWithin -Candidate $resolvedInput -AllowedRoot $allowedCriticRoot
    if ([System.IO.Path]::GetFileName($resolvedInput) -notmatch '^critic_(Q7|M2|R5|K8|V1)\.txt$') {
        throw "Unexpected critic input file: $resolvedInput"
    }
}
else {
    $allowedScorerRoot = Join-Path $challengeRunRoot 'inputs'
    $resolvedInput = Assert-PathWithin -Candidate $resolvedInput -AllowedRoot $allowedScorerRoot
    if ([System.IO.Path]::GetFileName($resolvedInput) -notmatch '^scorer_(Q7|M2|R5|K8|V1)_pass(1|2)\.txt$') {
        throw "Unexpected scorer input file: $resolvedInput"
    }
}

$resolvedAttestation = Assert-PathWithin -Candidate $AttestationPath -AllowedRoot (Join-Path $challengeRunRoot 'attestations')
$inputHash = Assert-Hash -Path $resolvedInput -Expected $ExpectedInputSha256
$inputBytes = [System.IO.File]::ReadAllBytes($resolvedInput)
$strictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)
$inputText = $strictUtf8.GetString($inputBytes)

$attestationParent = Split-Path -Parent $resolvedAttestation
if (-not (Test-Path -LiteralPath $attestationParent)) {
    New-Item -ItemType Directory -Path $attestationParent -Force | Out-Null
}
$attestation = [ordered]@{
    protocol = 'TFW55-I2-CATEGORY-FILEREAD-v4'
    status = 'verified_before_model_read'
    role = $Role
    input_path = $resolvedInput
    input_sha256 = $inputHash
    input_utf8_bytes = $inputBytes.Length
    frozen_v2_sha256 = $v2Hash
    category_v3_design_sha256 = $v3DesignHash
    category_v3_sha256sums_sha256 = $v3SumsHash
    verified_at_utc = [DateTime]::UtcNow.ToString('o')
}
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText(
    $resolvedAttestation,
    ($attestation | ConvertTo-Json -Depth 10 -Compress),
    $utf8NoBom
)

[Console]::OutputEncoding = $utf8NoBom
[Console]::Out.Write($inputText)
