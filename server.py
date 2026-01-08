import asyncio
import websockets
import json
import pyautogui

# --- CONFIGURAZIONE PRESTAZIONI ---
# Disabilita le pause interne per velocità massima
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False
SENSITIVITY = 1.8 # Modifica questo valore per mouse più/meno veloce

async def handler(websocket):
    print(f"Client connesso.")
    try:
        async for message in websocket:
            try:
                data = json.loads(message)
                
                # 1. Movimento (Ottimizzato)
                if data['type'] == 'move':
                    x = data['x'] * SENSITIVITY
                    y = data['y'] * SENSITIVITY
                    # _pause=False è fondamentale per la fluidità
                    pyautogui.moveRel(x, y, _pause=False)
                
                # 2. Click
                elif data['type'] == 'click':
                    pyautogui.click(button=data['btn'], _pause=False)
                
                # 3. Scrittura Testo
                elif data['type'] == 'text':
                    pyautogui.write(data['char'], _pause=False)
                
                # 4. Tasti Speciali (Invio, Backspace)
                elif data['type'] == 'key':
                    pyautogui.press(data['key'], _pause=False)

            except Exception as e:
                # Ignora errori di parsing per non bloccare il server
                pass
                    
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnesso.")

async def main():
    # ping_interval=None riduce l'overhead della rete
    print("--- LIQUID MOUSE SERVER ---")
    print("In attesa di connessione sulla porta 8765...")
    async with websockets.serve(handler, "0.0.0.0", 8765, ping_interval=None):
        await asyncio.Future()  # Esegui per sempre

if __name__ == "__main__":
    asyncio.run(main())
