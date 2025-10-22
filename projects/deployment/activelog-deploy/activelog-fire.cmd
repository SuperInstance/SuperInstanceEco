@echo off
REM === Usage: activelog-fire <source> <event> [logs]
REM Example: activelog-fire deck_sensor haul_start logs

IF "%~1"=="" (
    echo Usage: activelog-fire ^<source^> ^<event^> [logs]
    exit /b 1
)

IF "%~2"=="" (
    echo Usage: activelog-fire ^<source^> ^<event^> [logs]
    exit /b 1
)

set "SOURCE=%~1"
set "EVENT=%~2"
set "SHOWLOGS=%~3"
set "PAYLOAD={\"source\":\"%SOURCE%\",\"event\":\"%EVENT%\"}"

echo.
echo 🔹 Sending event: source=%SOURCE%, event=%EVENT%
echo.

aws lambda invoke ^
  --function-name activelog-logger ^
  --cli-binary-format raw-in-base64-out ^
  --payload "%PAYLOAD%" ^
  --region us-east-1 response.json >nul

echo ✅ Lambda invoked. Response:
type response.json
echo.

IF /I "%SHOWLOGS%"=="logs" (
    echo 📜 Tailing CloudWatch logs...
    aws logs tail /aws/lambda/activelog-logger --region us-east-1 --follow
)