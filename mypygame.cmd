@echo off
setlocal

call "%~dp0bootstrap.cmd" "%~dp0mypygame.py" %*
if errorlevel 1 (
    echo script failed
    exit /b 1
)
