@echo off
REM Script di avvio per Liquid Mouse Server

echo ================================================
echo    ^|^|  LIQUID MOUSE SERVER  ^|^|
echo ================================================
echo.

REM Controlla se Python è installato
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRORE] Python non trovato!
    echo Scarica Python da https://python.org
    echo.
    pause
    exit /b 1
)

REM Controlla se websockets è installato
python -m pip show websockets >nul 2>&1
if errorlevel 1 (
    echo [INFO] Installo dipendenze...
    python -m pip install websockets pyautogui
    if errorlevel 1 (
        echo [ERRORE] Fallita installazione dipendenze
        pause
        exit /b 1
    )
)

echo [OK] Dipendenze OK
echo.
echo Avvio server...
echo.

REM Cambia nella directory dello script (pushd supporta i percorsi UNC)
pushd "%~dp0"

python server.py

popd

pause
