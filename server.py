import asyncio
import websockets
import json
import pyautogui

# --- OTTIMIZZAZIONE PRESTAZIONI ---
# Disabilita la pausa di sicurezza di pyautogui (era 0.1s di default)
# Questo rende il movimento istantaneo.
pyautogui.PAUSE = 0 

# Riduce il failsafe per evitare blocchi accidentali agli angoli
pyautogui.FAILSAFE = False 

# Configurazione sensibilità
SENSITIVITY = 1.8

async def handler(websocket):
    print("Dispositivo connesso! (Modalità Turbo)")
    try:
        async for message in websocket:
            # Caricare il JSON è veloce, ma facciamolo in un blocco try per sicurezza
            try:
                data = json.loads(message)
                
                if data['type'] == 'move':
                    # Usiamo moveRel con _pause=False per forzare la velocità
                    # E arrotondiamo per evitare calcoli float inutili per i pixel
                    x = data['x'] * SENSITIVITY
                    y = data['y'] * SENSITIVITY
                    pyautogui.moveRel(x, y, _pause=False)
                    
                elif data['type'] == 'click':
                    if data['btn'] == 'left':
                        pyautogui.click(button='left', _pause=False)
                    elif data['btn'] == 'right':
                        pyautogui.click(button='right', _pause=False)

            except Exception as e:
                pass # Ignora errori di pacchetto per non fermare il flusso
                    
    except websockets.exceptions.ConnectionClosed:
        print("Disconnesso.")

async def main():
    # Ping interval None disabilita il ping/pong heartbeat per ridurre latenza
    async with websockets.serve(handler, "0.0.0.0", 8765, ping_interval=None):
        print("Server Ottimizzato in ascolto...")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
