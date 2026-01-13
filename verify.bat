@echo off
REM Quick Test Script for Liquid Mouse Pro
REM Verifica la configurazione e la disponibilità del sistema

setlocal enabledelayedexpansion

color 0A
cls

echo.
echo ╔═══════════════════════════════════════════════════════╗
echo ║     🖱️  LIQUID MOUSE PRO - SISTEMA DI CONTROLLO       ║
echo ║                                                       ║
echo ║  Versione: 1.0.0                                      ║
echo ║  Licenza: MIT                                         ║
echo ╚═══════════════════════════════════════════════════════╝
echo.
echo 📋 VERIFICA COMPONENTI...
echo.

REM Controlla Python
echo ⏳ Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python non trovato
    echo.
    echo   📥 Scarica Python da: https://python.org
    echo   ✅ Durante l'installazione, spunta "Add Python to PATH"
    echo.
    pause
    exit /b 1
) else (
    for /f "tokens=*" %%A in ('python --version') do set PYVER=%%A
    echo ✅ !PYVER! - OK
)

REM Controlla websockets
echo.
echo ⏳ Checking websockets module...
python -c "import websockets" >nul 2>&1
if errorlevel 1 (
    echo ❌ Modulo websockets non trovato
    echo ✅ Installazione in corso...
    python -m pip install websockets pyautogui
    if errorlevel 1 (
        echo ❌ Installazione fallita
        pause
        exit /b 1
    )
) else (
    echo ✅ websockets - Installato
)

REM Controlla pyautogui
echo.
echo ⏳ Checking pyautogui module...
python -c "import pyautogui" >nul 2>&1
if errorlevel 1 (
    echo ❌ Modulo pyautogui non trovato
    echo ✅ Installazione in corso...
    python -m pip install pyautogui
) else (
    echo ✅ pyautogui - Installato
)

echo.
echo ═══════════════════════════════════════════════════════
echo.
echo ✅ TUTTO OK! Il sistema è pronto per l'uso.
echo.
echo 🚀 PROSSIMI PASSI:
echo.
echo   1️⃣  Esegui il server:
echo       python server.py
echo.
echo   2️⃣  Dal tuo smartphone apri:
echo       http://[IP-DEL-COMPUTER]:8000
echo.
echo   3️⃣  Configurazione rapida:
echo       - Inserisci l'IP mostrato nel terminale
echo       - Tocca il pulsante CONNETTI
echo       - Controlla che appaia "LINKED" in verde
echo.
echo ═══════════════════════════════════════════════════════
echo.
pause
