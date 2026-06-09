@echo off
title ServerWatch v1.0 - Status Check
color 0b
echo ===================================================
echo             SERVERWATCH IS STARTING           
echo ===================================================
echo.
echo [*] Checking required libraries...
echo [*] Please wait, this may take a moment on the first run.
echo.

:: Arka plandaki yükleme yazılarını gizler ve kütüphaneleri kurar
python -m pip install customtkinter mcstatus >nul 2>&1

echo [OK] Libraries are ready! Opening panel...
echo.
echo [NOTE] You can close this command window anytime.
echo        The program will keep running in the background.
echo.

:: Programı tamamen bağımsız başlatır
start pythonw main.py

:: CMD ekranının kendi kendine kapanmasını engeller
pause