@echo off
echo Stopping any existing backend processes on port 8000...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8000') do taskkill /f /pid %%a 2>nul
timeout /t 3 /nobreak >nul
echo Starting backend server on port 8000...
cd backend
start /b uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload --timeout-keep-alive 30 --log-level info > backend.log 2>&1
echo Backend server started successfully on port 8000
timeout /t 5 /nobreak >nul
echo Checking if server is running...
netstat -an | findstr :8000 >nul
if %errorlevel% equ 0 (
    echo Server is running on port 8000
    echo You can now access the API at http://localhost:8000
) else (
    echo Error: Server failed to start. Check backend.log for details.
)