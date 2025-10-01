@echo off
REM Script untuk setup dan testing AWS LocalStack di Windows

echo === AWS LocalStack Setup Script untuk Windows ===

if "%1"=="start" goto start
if "%1"=="stop" goto stop
if "%1"=="restart" goto restart
if "%1"=="reset" goto reset
if "%1"=="status" goto status
if "%1"=="test" goto test
goto usage

:start
echo Starting LocalStack...
docker-compose up -d
echo Waiting for LocalStack to be ready...
timeout /t 10 /nobreak > nul
call :check_status
if %errorlevel%==0 (
    echo LocalStack is ready!
) else (
    echo LocalStack might still be starting up. Check manually with: curl http://localhost:4566/health
)
goto end

:stop
echo Stopping LocalStack...
docker-compose down
goto end

:restart
call :stop
call :start
goto end

:reset
echo Resetting LocalStack data...
docker-compose down
if exist localstack_data rmdir /s /q localstack_data
echo Data reset complete
goto end

:status
call :check_status
if %errorlevel%==0 (
    echo LocalStack is running
) else (
    echo LocalStack is not running
)
goto end

:test
call :check_status
if %errorlevel%==0 (
    echo Running tests...
    call :test_s3
    call :test_dynamodb
) else (
    echo Please start LocalStack first: setup.bat start
)
goto end

:check_status
curl -s http://localhost:4566/health > nul 2>&1
exit /b %errorlevel%

:test_s3
echo === Testing S3 ===
echo Creating S3 bucket...
for /f "tokens=2 delims==" %%i in ('wmic OS Get localdatetime /value') do set datetime=%%i
set bucket_name=test-bucket-%datetime:~0,14%
aws --endpoint-url=http://localhost:4566 s3 mb s3://%bucket_name%
echo Listing S3 buckets...
aws --endpoint-url=http://localhost:4566 s3 ls
goto :eof

:test_dynamodb
echo === Testing DynamoDB ===
echo Creating DynamoDB table...
for /f "tokens=2 delims==" %%i in ('wmic OS Get localdatetime /value') do set datetime=%%i
set table_name=test-table-%datetime:~0,14%
aws --endpoint-url=http://localhost:4566 dynamodb create-table --table-name %table_name% --attribute-definitions AttributeName=id,AttributeType=S --key-schema AttributeName=id,KeyType=HASH --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
echo Listing DynamoDB tables...
aws --endpoint-url=http://localhost:4566 dynamodb list-tables
goto :eof

:usage
echo Usage: %0 {start^|stop^|restart^|reset^|status^|test}
echo.
echo Commands:
echo   start   - Start LocalStack
echo   stop    - Stop LocalStack
echo   restart - Restart LocalStack
echo   reset   - Reset all LocalStack data
echo   status  - Check LocalStack status
echo   test    - Run test commands
goto end

:end