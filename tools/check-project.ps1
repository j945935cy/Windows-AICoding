$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

function Count-Files($path, $filter) {
  return (Get-ChildItem -Path $path -Filter $filter -File | Measure-Object).Count
}

$chapterMarkdownCount = Count-Files "chapters" "ch*.md"
$chapterHtmlCount = Count-Files "chapters" "ch*.html"
$appendixMarkdownCount = Count-Files "appendices" "*.md"
$appendixHtmlCount = Count-Files "appendices" "*.html"
$exampleCount = (Get-ChildItem -Path "examples" -Directory | Measure-Object).Count

Write-Host "AI Coding 入門 project check"
Write-Host "----------------------------"
Write-Host "Chapter markdown: $chapterMarkdownCount"
Write-Host "Chapter html:     $chapterHtmlCount"
Write-Host "Appendix md:      $appendixMarkdownCount"
Write-Host "Appendix html:    $appendixHtmlCount"
Write-Host "Examples:         $exampleCount"
Write-Host ""

$expected = @(
  @{ Name = "chapter markdown"; Actual = $chapterMarkdownCount; Expected = 18 },
  @{ Name = "chapter html"; Actual = $chapterHtmlCount; Expected = 18 },
  @{ Name = "appendix markdown"; Actual = $appendixMarkdownCount; Expected = 6 },
  @{ Name = "appendix html"; Actual = $appendixHtmlCount; Expected = 6 },
  @{ Name = "examples"; Actual = $exampleCount; Expected = 16 }
)

$failed = $false

foreach ($item in $expected) {
  if ($item.Actual -ne $item.Expected) {
    Write-Host "Count mismatch: $($item.Name) expected $($item.Expected), got $($item.Actual)" -ForegroundColor Red
    $failed = $true
  }
}

$requiredFiles = @(
  "index.html",
  "chapters.html",
  "projects.html",
  "examples.html",
  "appendices.html",
  "progress.html",
  "manuscript.html",
  "search.html",
  "print.html",
  "style.css",
  "print.css",
  "script.js",
  "progress.js",
  "search.js",
  "README.md",
  "BOOK.md",
  "book.html",
  "EXPORT.md",
  "CONTRIBUTING.md",
  "EDITORIAL_REVIEW.md",
  "RELEASE_CHECKLIST.md"
)

foreach ($file in $requiredFiles) {
  if (-not (Test-Path -LiteralPath $file)) {
    Write-Host "Missing required file: $file" -ForegroundColor Red
    $failed = $true
  }
}

$missingLinks = @()
$htmlFiles = Get-ChildItem -Recurse -Include *.html -File

foreach ($file in $htmlFiles) {
  $text = Get-Content -Raw -Encoding UTF8 -LiteralPath $file.FullName
  [regex]::Matches($text, 'href="([^"]+)"|src="([^"]+)"') | ForEach-Object {
    $target = if ($_.Groups[1].Value) { $_.Groups[1].Value } else { $_.Groups[2].Value }

    if ($target -match '^(https?:|mailto:|#)' -or $target -match '^$') {
      return
    }

    $clean = ($target -split '#')[0]

    if ($clean -eq '') {
      return
    }

    $resolved = Join-Path $file.DirectoryName $clean

    if (-not (Test-Path -LiteralPath $resolved)) {
      $missingLinks += [pscustomobject]@{
        File = $file.FullName
        Target = $target
      }
    }
  }
}

if ($missingLinks.Count -gt 0) {
  Write-Host ""
  Write-Host "Missing local links:" -ForegroundColor Red
  $missingLinks | Format-Table -AutoSize
  $failed = $true
}

if ($failed) {
  Write-Host ""
  Write-Host "Project check failed." -ForegroundColor Red
  exit 1
}

Write-Host "Project check passed." -ForegroundColor Green
