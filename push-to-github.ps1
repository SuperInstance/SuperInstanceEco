# Push ActiveLog Technical Repository to GitHub
# Run this from PowerShell or Git Bash

Write-Host "Pushing ActiveLog-TechnicalRepo to GitHub..." -ForegroundColor Green

# Navigate to repository
Set-Location $PSScriptRoot

# Check if repository exists
if (-not (Test-Path ".git")) {
    Write-Host "Error: Not a git repository" -ForegroundColor Red
    exit 1
}

# Show status
Write-Host "`nRepository Status:" -ForegroundColor Yellow
git status

# Show what will be pushed
Write-Host "`nCommit to be pushed:" -ForegroundColor Yellow
git log -1 --oneline

# Push to GitHub
Write-Host "`nPushing to GitHub..." -ForegroundColor Green
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ Successfully pushed to GitHub!" -ForegroundColor Green
    Write-Host "Repository: https://github.com/ctothed/SuperInstance" -ForegroundColor Cyan
} else {
    Write-Host "`n❌ Push failed. Please check your GitHub credentials." -ForegroundColor Red
    Write-Host "Try running: gh auth login" -ForegroundColor Yellow
}
