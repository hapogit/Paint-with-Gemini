@echo off
REM Script di avvio per Liquid Mouse
REM Avvia l'applicazione senza mostrare la console nera

echo ================================================
echo       LIQUID MOUSE - AVVIO IN CORSO...
echo ================================================
echo.

REM 1. Verifica Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRORE] Python non trovato!
    echo Scarica Python da https://python.org e spunta "Add to PATH".
    pause
    exit /b 1
)

REM 2. Verifica Dipendenze essenziali
python -c "import websockets; import pyautogui; import pystray; import PIL" >nul 2>&1
if errorlevel 1 (
    echo [INFO] Installazione dipendenze mancanti...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERRORE] Impossibile installare le dipendenze.
        pause
        exit /b 1
    )
)

REM 3. Avvia l'applicazione (server.pyw) in background
echo [OK] Avvio dell'interfaccia grafica...
start "" pythonw server.pyw

REM Chiude questa finestra cmd immediatamente
exit