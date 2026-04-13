param(
    [Parameter(Mandatory = $true, HelpMessage = "The podcast folder name to process.")]
    [ValidateNotNullOrEmpty()]
    [string]$PodcastFolder,

    [Parameter(Mandatory = $true, HelpMessage = "Prefix used to build release tags (for example: rfc).")]
    [ValidateNotNullOrEmpty()]
    [string]$TagPrefix
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$SuccessColor = "Green"
$WarningColor = "Yellow"
$ErrorColor = "Red"
$InfoColor = "Cyan"

function Write-ColoredOutput {
    param(
        [string]$Message,
        [string]$Color = "White"
    )

    Write-Host $Message -ForegroundColor $Color
}

function Invoke-GhCommand {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$Arguments
    )

    $hasNativePreference = Test-Path -LiteralPath "Variable:\PSNativeCommandUseErrorActionPreference"
    if ($hasNativePreference) {
        $previousNativePreference = $PSNativeCommandUseErrorActionPreference
        $PSNativeCommandUseErrorActionPreference = $false
    }

    $output = @()
    $exitCode = 0

    try {
        $output = & gh @Arguments 2>&1
        $exitCode = $LASTEXITCODE
    } catch {
        if ($LASTEXITCODE -ne $null -and $LASTEXITCODE -ne 0) {
            $exitCode = $LASTEXITCODE
        } else {
            $exitCode = 1
        }

        $output = @($output + $_.ToString())
    } finally {
        if ($hasNativePreference) {
            $PSNativeCommandUseErrorActionPreference = $previousNativePreference
        }
    }

    return [PSCustomObject]@{
        ExitCode = $exitCode
        Output = $output
        OutputText = ($output | Out-String).Trim()
    }
}

function Test-ReleaseExists {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Tag
    )

    $result = Invoke-GhCommand -Arguments @("release", "view", $Tag)
    if ($result.ExitCode -eq 0) {
        return $true
    }

    if ($result.OutputText -match "(?i)(release\s+not\s+found|not\s+found|http\s+404|404\s+not\s+found)") {
        return $false
    }

    # If view fails for an unexpected reason, continue to create and let create provide the definitive error.
    Write-ColoredOutput "  [WARN] Could not verify existing release '$Tag'. Attempting create anyway. gh output: $($result.OutputText)" -Color $WarningColor
    return $false
}

if ($TagPrefix -notmatch "^[A-Za-z0-9][A-Za-z0-9._-]*$") {
    Write-ColoredOutput "ERROR: TagPrefix '$TagPrefix' is invalid. Use letters, numbers, dot, underscore, and hyphen only." -Color $ErrorColor
    exit 1
}

$basePath = (Get-Location).ProviderPath
$podcastPath = Join-Path -Path $basePath -ChildPath $PodcastFolder

if (-not (Test-Path -LiteralPath $podcastPath -PathType Container)) {
    Write-ColoredOutput "ERROR: Podcast folder '$PodcastFolder' not found at '$podcastPath'." -Color $ErrorColor
    exit 1
}

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-ColoredOutput "ERROR: GitHub CLI ('gh') was not found on PATH." -Color $ErrorColor
    exit 1
}

$authResult = Invoke-GhCommand -Arguments @("auth", "status")
if ($authResult.ExitCode -ne 0) {
    Write-ColoredOutput "ERROR: GitHub CLI is not authenticated. Run 'gh auth login' first." -Color $ErrorColor
    exit 1
}

$yearFolders = Get-ChildItem -LiteralPath $podcastPath -Directory |
    Where-Object { $_.Name -match "^\d{4}(?:-\d{4})?$" } |
    Sort-Object @{ Expression = { [int]([regex]::Match($_.Name, "^\d{4}").Value) } }, @{ Expression = { $_.Name } }

if ($yearFolders.Count -eq 0) {
    Write-ColoredOutput "No year folders found in '$PodcastFolder'." -Color $WarningColor
    exit 0
}

Write-ColoredOutput "`n========================================" -Color $SuccessColor
Write-ColoredOutput "PODCAST RELEASE PUBLISH SCRIPT" -Color $SuccessColor
Write-ColoredOutput "========================================`n" -Color $SuccessColor
Write-ColoredOutput "Podcast folder: $PodcastFolder" -Color $InfoColor
Write-ColoredOutput "Tag prefix: $TagPrefix" -Color $InfoColor
Write-ColoredOutput "Podcast path: $podcastPath`n" -Color $InfoColor

$seenTags = @{}
$createdCount = 0
$skippedCount = 0
$failedCount = 0
$currentYear = 2026

foreach ($yearFolder in $yearFolders) {
    $year = [regex]::Match($yearFolder.Name, "^\d{4}").Value
    if ([int]$year -eq $currentYear) {
        Write-ColoredOutput "  [SKIP] Skipping current year folder '$($yearFolder.Name)'." -Color $WarningColor
        $skippedCount++
        continue
    }

    $tag = "$TagPrefix-$year"
    $zipFileName = "$year.zip"
    $zipPath = Join-Path -Path $yearFolder.FullName -ChildPath $zipFileName

    Write-ColoredOutput "-------------------------------------------" -Color $InfoColor
    Write-ColoredOutput "Processing folder: $($yearFolder.Name)" -Color $InfoColor
    Write-ColoredOutput "Tag: $tag" -Color $InfoColor
    Write-ColoredOutput "-------------------------------------------" -Color $InfoColor

    if ($seenTags.ContainsKey($tag)) {
        Write-ColoredOutput "  [SKIP] Duplicate computed tag '$tag' from folder '$($yearFolder.Name)'." -Color $WarningColor
        $skippedCount++
        continue
    }

    $seenTags[$tag] = $true

    if (-not (Test-Path -LiteralPath $zipPath -PathType Leaf)) {
        Write-ColoredOutput "  [SKIP] Missing archive '$zipFileName'." -Color $WarningColor
        $skippedCount++
        continue
    }

    try {
        if (Test-ReleaseExists -Tag $tag) {
            Write-ColoredOutput "  [SKIP] Release '$tag' already exists." -Color $WarningColor
            $skippedCount++
            continue
        }

        $title = "$year $PodcastFolder Transcripts"
        $notes = @"
# $year $PodcastFolder Transcripts
Complete transcripts from the $year episodes of the $PodcastFolder.
Generated from [this GitHub repository](https://github.com/willtheorangeguy/Changelog-Transcripts).
"@

        $createResult = Invoke-GhCommand -Arguments @("release", "create", $tag, $zipPath, "--title", $title, "--notes", $notes)
        if ($createResult.ExitCode -ne 0) {
            if ($createResult.OutputText -match "(?i)(already\s+exists|release.+already.+exists|tag.+already.+exists)") {
                Write-ColoredOutput "  [SKIP] Release '$tag' already exists." -Color $WarningColor
                $skippedCount++
                continue
            }

            throw "gh release create failed for '$tag'. gh output: $($createResult.OutputText)"
        }

        Write-ColoredOutput "  [OK] Published release '$tag' with asset '$zipFileName'." -Color $SuccessColor
        $createdCount++
    } catch {
        Write-ColoredOutput "  [ERROR] $($_.Exception.Message)" -Color $ErrorColor
        $failedCount++
    }
}

Write-ColoredOutput "`n========================================" -Color $SuccessColor
Write-ColoredOutput "SUMMARY" -Color $SuccessColor
Write-ColoredOutput "========================================" -Color $SuccessColor
Write-ColoredOutput "Releases created: $createdCount" -Color $SuccessColor
Write-ColoredOutput "Years skipped: $skippedCount" -Color $InfoColor
Write-ColoredOutput "Years failed: $failedCount`n" -Color $InfoColor

if ($failedCount -gt 0) {
    exit 1
}

exit 0
