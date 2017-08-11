@echo off
setlocal

set python_path=%~dp0Scripts\python.exe
set pip_path=%~dp0Scripts\pip.exe

if not exist "%python_path%" (
    cd /d "%~dp0"
    python -m virtualenv .
    if errorlevel 1 (
        echo virtualenv failed
        exit /b 1
    )
)

"%pip_path%" install -q -r "%~dp0requirements.txt"
if errorlevel 1 (
    echo pip failed
    exit /b 1
)

"%python_path%" %*
if errorlevel 1 (
    echo script failed
    exit /b 1
)
