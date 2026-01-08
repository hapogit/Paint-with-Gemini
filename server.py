import asyncio
import websockets
import json
import pyautogui

# Configurazione sensibilità
SENSITIVITY = 1.5
pyautogui.FAILSAFE = False # Attenzione: permette al mouse di andare agli angoli

async def handler(websocket):
    print("Dispositivo connesso!")
    try:
        async for message in websocket:
            data = json.loads(message)
            
            if data['type'] == 'move':
                # Muovi il mouse relativo alla posizione attuale
                x = data['x'] * SENSITIVITY
                y = data['y'] * SENSITIVITY
                pyautogui.moveRel(x, y)
                
            elif data['type'] == 'click':
                # Esegui il click
                if data['btn'] == 'left':
                    pyautogui.click(button='left')
                elif data['btn'] == 'right':
                    pyautogui.click(button='right')
                    
    except websockets.exceptions.ConnectionClosed:
        print("Dispositivo disconnesso.")

async def main():
    # Ascolta su tutte le interfacce di rete (0.0.0.0) alla porta 8765
    print("Server Liquid Mouse avviato...")
    print("Trova il tuo IP locale (es. ipconfig su Windows) e inseriscilo nel file HTML.")
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
