@echo off
echo Testing backend API connectivity...
echo.

curl -X GET http://localhost:8000/ --header "Content-Type: application/json"
echo.
echo.
curl -X GET http://localhost:8000/health --header "Content-Type: application/json"
echo.
echo API test completed.