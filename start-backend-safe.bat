@echo off
echo Stopping any existing backend processes on port 8000...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8000') do taskkill /f /pid %%a 2>nul
timeout /t 2 /nobreak >nul
echo Starting backend server on port 8000...
cd backend
start /b uvicorn src.main:app --host 0.0.0.0 --port 8000 --workers 4 --timeout-keep-alive 30 --log-level info > backend.log 2>&1
echo Backend server started successfully on port 8000