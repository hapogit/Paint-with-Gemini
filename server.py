"""
🖱️ LIQUID MOUSE PRO - Server WebSocket
======================================

Un'applicazione per controllare il mouse e la tastiera del PC 
tramite smartphone utilizzando WebSocket.

Versione: 1.0.0
Licenza: MIT
Autore: Liquid Mouse Pro Team
Repository: https://github.com/tuouser/liquid-mouse-pro

Uso:
    python server.py

    Quindi apri dal tuo smartphone:
    http://[IP-DEL-COMPUTER]:8000
"""

import asyncio
import websockets
import json
import pyautogui
import socket
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

# --- CONFIGURAZIONE PRESTAZIONI ---
# Disabilita le pause interne per velocità massima
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False
SENSITIVITY = 1.8  # Modifica questo valore per mouse più/meno veloce
PORT = 8765
HTTP_PORT = 8000

# --- FUNZIONE PER OTTENERE L'IP LOCALE ---
def get_local_ip():
    """Ottiene l'indirizzo IP locale del computer"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Connessione fittizia per ottenere l'IP
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

async def handler(websocket):
    print(f"Client connesso.")
    try:
        async for message in websocket:
            try:
                data = json.loads(message)
                msg_type = data.get('type', '')
                
                # 1. Movimento (Ottimizzato)
                if msg_type == 'move':
                    x = int(float(data.get('x', 0)) * SENSITIVITY)
                    y = int(float(data.get('y', 0)) * SENSITIVITY)
                    if x != 0 or y != 0:
                        pyautogui.moveRel(x, y, _pause=False)
                
                # 2. Scroll verticale
                elif msg_type == 'scroll':
                    scroll_amount = int(data.get('amount', 0))
                    if scroll_amount != 0:
                        pyautogui.scroll(scroll_amount, _pause=False)
                
                # 3. Click
                elif msg_type == 'click':
                    btn = data.get('btn', 'left')
                    pyautogui.click(button=btn, _pause=False)
                
                # 4. Scrittura Testo (singoli caratteri)
                elif msg_type == 'text':
                    char = data.get('char', '')
                    if char:
                        # Usa typewrite per caratteri speciali
                        pyautogui.typewrite(char, interval=0.05) if len(char) == 1 else pyautogui.write(char, _pause=False)
                        print(f"Carattere scritto: '{char}'")
                
                # 5. Tasti Speciali
                elif msg_type == 'key':
                    key = data.get('key', '')
                    if key:
                        pyautogui.press(key, _pause=False)
                        print(f"Tasto premuto: {key}")

            except json.JSONDecodeError as e:
                print(f"Errore JSON: {e}")
            except Exception as e:
                print(f"Errore: {e}")
                import traceback
                traceback.print_exc()
                    
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnesso.")

def start_http_server(port):
    """Avvia il server HTTP per servire index.html"""
    class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/' or self.path == '':
                self.path = '/index.html'
            return SimpleHTTPRequestHandler.do_GET(self)
        
        def log_message(self, format, *args):
            # Silenzioso per evitare log troppo verbosi
            pass
    
    handler = MyHTTPRequestHandler
    httpd = HTTPServer(("0.0.0.0", port), handler)
    print(f"✅ Server HTTP avviato sulla porta {port}")
    httpd.serve_forever()

async def main():
    # ping_interval=None riduce l'overhead della rete
    ip = get_local_ip()
    
    # Cambia la directory di lavoro per servire index.html
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Avvia il server HTTP in un thread separato
    import threading
    http_thread = threading.Thread(target=start_http_server, args=(HTTP_PORT,), daemon=True)
    http_thread.start()
    
    print("\n" + "="*50)
    print("   🖱️  LIQUID MOUSE SERVER")
    print("="*50)
    print(f"📡 IP Locale: {ip}")
    print(f"🌐 WebSocket: ws://{ip}:{PORT}")
    print(f"🌐 HTTP: http://{ip}:{HTTP_PORT}")
    print("="*50)
    print("\n📱 Apri questo link sul tuo smartphone:")
    print(f"   http://{ip}:{HTTP_PORT}")
    print("\n⏳ In attesa di connessione...")
    print("="*50 + "\n")
    
    async with websockets.serve(handler, "0.0.0.0", PORT, ping_interval=None):
        await asyncio.Future()  # Esegui per sempre

if __name__ == "__main__":
    asyncio.run(main())
