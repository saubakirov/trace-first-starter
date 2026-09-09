param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[0-9a-fA-F]{40}$')]
    [string]$CandidateSha,
    [Parameter(Mandatory = $true)]
    [string]$OutputDirectory
)
$slcBaseline = 'affd9033abf94e9b9a9e27114f3bfbb16066438a'
$valuePaths = @(
    '.tfw/templates/project_config.yaml'
    '.tfw/project_config.yaml'
    '.tfw/knowledge_state.yaml'
    '.tfw/conventions.md'
    '.tfw/compilable_contract.md'
    '.tfw/quickstart.md'
    '.tfw/workflows/init.md'
    '.tfw/workflows/resume.md'
    '.tfw/workflows/knowledge.md'
    '.tfw/workflows/update.md'
    'tools/tfw_state.py'
    'docs/scripts/gen_docs.py'
    'tasks/README.md'
    '.claude/commands/tfw-init.md'
    '.claude/commands/tfw-resume.md'
    '.claude/commands/tfw-knowledge.md'
    '.claude/commands/tfw-update.md'
    '.agents/workflows/tfw-init.md'
    '.agents/workflows/tfw-resume.md'
    '.agents/workflows/tfw-knowledge.md'
    '.agents/workflows/tfw-update.md'
    '.tfw/VERSION'
    '.tfw/CHANGELOG.md'
    '.tfw/migrations/3.3.0.md'
)
$slcResolvedCandidate = git rev-parse --verify ($CandidateSha + '^{commit}')
if ($LASTEXITCODE -ne 0 -or $slcResolvedCandidate -ine $CandidateSha) {
    throw 'CandidateSha must identify an existing commit by its exact full SHA.'
}
$slcOutput = (Resolve-Path -LiteralPath $OutputDirectory -ErrorAction Stop).ProviderPath
$slcNames = Join-Path $slcOutput ('slc-' + $CandidateSha + '-name-status.z')
$slcNumstat = Join-Path $slcOutput ('slc-' + $CandidateSha + '-numstat.z')
if ((Test-Path -LiteralPath $slcNames) -or (Test-Path -LiteralPath $slcNumstat)) {
    throw 'Use a fresh accounting directory; preserve earlier measurement attachments.'
}
git --literal-pathspecs diff --no-ext-diff --name-status --find-renames=50% -z --output=$slcNames $slcBaseline $CandidateSha -- $valuePaths
if ($LASTEXITCODE -ne 0) { throw 'SLC name-status measurement failed.' }
git --literal-pathspecs diff --no-ext-diff --numstat --find-renames=50% -z --output=$slcNumstat $slcBaseline $CandidateSha -- $valuePaths
if ($LASTEXITCODE -ne 0) { throw 'SLC numstat measurement failed.' }
