@echo off
echo Starting production-ready backend deployment...

REM Kill any existing processes on port 8000
echo Stopping existing processes...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8000') do taskkill /f /pid %%a 2>nul

REM Wait for port to be released
timeout /t 3 /nobreak >nul

REM Start the backend with proper error handling
cd backend
echo Starting backend server...
start /b python -m uvicorn src.main:app --host 0.0.0.0 --port 8000 --workers 4 --timeout-keep-alive 30 --log-level info > backend.log 2>&1

REM Verify the server started
timeout /t 5 /nobreak >nul
netstat -an | findstr :8000 >nul
if %errorlevel% equ 0 (
    echo Backend server is running on port 8000
) else (
    echo Error: Backend server failed to start. Check backend.log for details.
)

echo Deployment completed.