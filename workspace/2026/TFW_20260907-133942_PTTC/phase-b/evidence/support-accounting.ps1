param([Parameter(Mandatory=$true)][string]$Candidate)
$ErrorActionPreference = 'Stop'
$taskRepo = 'C:/Users/c0rpa/.codex/worktrees/04a4/steps-framework'
$taskOut = Join-Path $taskRepo 'workspace/2026/TFW_20260907-133942_PTTC/phase-b/evidence'
$candidateSha = $Candidate
if ($candidateSha -notmatch '^[0-9a-f]{40}$') { throw 'Full Candidate SHA required' }
$valuePaths = @(
  '.tfw/conventions.md',
  '.tfw/workflows/handoff.md',
  '.tfw/workflows/review.md',
  '.tfw/workflows/docs.md',
  '.tfw/workflows/knowledge.md',
  '.tfw/workflows/resume.md',
  '.tfw/templates/status.md',
  '.tfw/templates/journal/event.md',
  '.tfw/templates/REVIEW.md',
  '.tfw/templates/review/verify.md',
  '.tfw/templates/evidence/EV.md',
  '.claude/commands/tfw-handoff.md',
  '.claude/commands/tfw-review.md',
  '.claude/commands/tfw-docs.md',
  '.claude/commands/tfw-knowledge.md',
  '.claude/commands/tfw-resume.md',
  '.agents/workflows/tfw-handoff.md',
  '.agents/workflows/tfw-review.md',
  '.agents/workflows/tfw-docs.md',
  '.agents/workflows/tfw-knowledge.md',
  '.agents/workflows/tfw-resume.md',
  '.tfw/adapters/codex/skills/tfw-review/SKILL.md',
  '.tfw/adapters/codex/skills/tfw-resume/SKILL.md',
  '.agents/skills/tfw-review/SKILL.md',
  '.agents/skills/tfw-resume/SKILL.md'
)
# Same approved git argv; copy stdout bytes directly, preserving every NUL.
foreach ($taskMode in @('--name-status','--numstat')) {
  $taskArgs = @('diff',$taskMode,'--find-renames=50%','-z','982a41841bea4cff2e253a98d6e0db008a7f7194',$candidateSha,'--') + $valuePaths
  $taskName = if ($taskMode -eq '--name-status') {'accounting-name-status.nul'} else {'accounting-numstat.nul'}
  $taskInfo = [Diagnostics.ProcessStartInfo]::new()
  $taskInfo.FileName = 'git'
  $taskInfo.WorkingDirectory = $taskRepo
  $taskInfo.UseShellExecute = $false
  $taskInfo.CreateNoWindow = $true
  $taskInfo.RedirectStandardOutput = $true
  $taskInfo.RedirectStandardError = $true
  $taskInfo.Arguments = ($taskArgs | ForEach-Object { '"' + $_ + '"' }) -join ' '
  $taskProcess = [Diagnostics.Process]::Start($taskInfo)
  $taskStream = [IO.File]::Create((Join-Path $taskOut $taskName))
  try { $taskProcess.StandardOutput.BaseStream.CopyTo($taskStream) } finally { $taskStream.Dispose() }
  $taskError = $taskProcess.StandardError.ReadToEnd()
  $taskProcess.WaitForExit()
  if ($taskProcess.ExitCode -ne 0) { throw $taskError }
  Write-Output ($taskArgs -join ' ')
}
$taskAccounting = @{baseline='982a41841bea4cff2e253a98d6e0db008a7f7194';candidate=$candidateSha;selector=$valuePaths;planned_files=25;planned_touched_loc=2400;approval='37f5a2ae66431b687c16fa65ee302c5948e96349'}
[IO.File]::WriteAllText((Join-Path $taskOut 'accounting-inputs.json'),($taskAccounting | ConvertTo-Json -Depth 5),[Text.UTF8Encoding]::new($false))
