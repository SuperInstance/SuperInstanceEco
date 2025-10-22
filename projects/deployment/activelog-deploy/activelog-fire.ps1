param (
    [Parameter(Mandatory = $true)]
    [string]$Source,

    [Parameter(Mandatory = $true)]
    [string]$Event,

    [switch]$Logs
)

# Build JSON payload safely
$payloadObj = @{
    source = $Source
    event  = $Event
}

$payloadJson = $payloadObj | ConvertTo-Json -Compress

Write-Host ""
Write-Host "Sending event: source=$Source, event=$Event"
Write-Host ""

# Invoke Lambda with raw JSON, wrapped to avoid CLI parse warnings
aws lambda invoke `
    --function-name activelog-logger `
    --cli-binary-format raw-in-base64-out `
    --payload "'$payloadJson'" `
    --region us-east-1 response.json | Out-Null

Write-Host "Lambda invoked. Response:"
Get-Content response.json
Write-Host ""

# Optional CloudWatch tail
if ($Logs) {
    Write-Host "Tailing CloudWatch logs..."
    aws logs tail /aws/lambda/activelog-logger --region us-east-1 --follow
}