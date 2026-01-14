"""
🖱️ LIQUID MOUSE - Server Application
====================================
Versione: 1.2.0
Descrizione: Server WebSocket con interfaccia GUI e supporto System Tray.
Licenza: MIT
"""

import asyncio
import websockets
import json
import pyautogui
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import sys

# --- MODULI SYSTEM TRAY ---
import pystray
from PIL import Image, ImageDraw

# --- CONFIGURAZIONE SISTEMA ---
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False
SENSITIVITY = 1.8 
PORT = 8765
HTTP_PORT = 8000

# --- PALETTE COLORI (Design System) ---
COLOR_BG = "#2b2e4a"       # Background principale
COLOR_TEXT = "#ffffff"     # Testo primario
COLOR_ACCENT = "#88ffcc"   # Accento (Verde acqua)
COLOR_LOG_BG = "#1f2235"   # Background area log
COLOR_LOG_TEXT = "#00ff00" # Testo terminale

# --- UTILITIES DI RETE ---
def get_local_ip():
    """Recupera l'indirizzo IP locale della macchina host."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

# --- LOGICA SERVER WEBSOCKET (Backend) ---
async def handler(websocket):
    log_message(f"Dispositivo connesso.")
    try:
        async for message in websocket:
            try:
                data = json.loads(message)
                msg_type = data.get('type', '')
                
                # Gestione Movimento Cursore
                if msg_type == 'move':
                    x = int(float(data.get('x', 0)) * SENSITIVITY)
                    y = int(float(data.get('y', 0)) * SENSITIVITY)
                    if x != 0 or y != 0:
                        pyautogui.moveRel(x, y, _pause=False)
                
                # Gestione Scorrimento (Scroll)
                elif msg_type == 'scroll':
                    scroll_amount = int(data.get('amount', 0))
                    if scroll_amount != 0:
                        pyautogui.scroll(scroll_amount, _pause=False)
                
                # Gestione Click Mouse
                elif msg_type == 'click':
                    btn = data.get('btn', 'left')
                    pyautogui.click(button=btn, _pause=False)
                
                # Gestione Input Testo
                elif msg_type == 'text':
                    char = data.get('char', '')
                    if char:
                        pyautogui.typewrite(char, interval=0.05) if len(char) == 1 else pyautogui.write(char, _pause=False)
                
                # Gestione Tasti Speciali
                elif msg_type == 'key':
                    key = data.get('key', '')
                    if key:
                        pyautogui.press(key, _pause=False)
                        log_message(f"Input Tasto: {key}")

                # Gestione Trascinamento (Drag & Drop)
                elif msg_type == 'drag':
                    state = data.get('state', 'up')
                    if state == 'down':
                        pyautogui.mouseDown(button='left', _pause=False)
                        log_message("Modalità Drag: ATTIVA")
                    else:
                        pyautogui.mouseUp(button='left', _pause=False)
                        log_message("Modalità Drag: DISATTIVA")

                # Gestione Scorciatoie (Hotkeys)
                elif msg_type == 'hotkey':
                    keys = data.get('keys', [])
                    if keys:
                        pyautogui.hotkey(*keys)
                        log_message(f"Esecuzione Hotkey: {keys}")

            except Exception as e:
                log_message(f"Errore elaborazione: {e}")
                    
    except websockets.exceptions.ConnectionClosed:
        log_message("Dispositivo disconnesso.")
    finally:
        # Sicurezza: Rilascia il mouse in caso di disconnessione improvvisa
        pyautogui.mouseUp(button='left')

def start_http_server(port):
    """Avvia il server HTTP per servire l'interfaccia client."""
    class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/' or self.path == '':
                self.path = '/index.html'
            return SimpleHTTPRequestHandler.do_GET(self)
        def log_message(self, format, *args):
            pass # Sopprime i log HTTP standard
    
    handler = MyHTTPRequestHandler
    httpd = HTTPServer(("0.0.0.0", port), handler)
    log_message(f"Servizio HTTP avviato sulla porta {port}")
    httpd.serve_forever()

async def start_websocket_server():
    """Inizializza il server WebSocket asincrono."""
    ip = get_local_ip()
    update_ui_info(ip)
    
    log_message("="*30)
    log_message("   LIQUID MOUSE - SERVER ONLINE")
    log_message("="*30)
    log_message(f"Indirizzo IP Host: {ip}")
    log_message("In attesa di connessione client...")
    
    async with websockets.serve(handler, "0.0.0.0", PORT, ping_interval=None):
        await asyncio.Future()

def run_services():
    """Coordina l'avvio dei servizi HTTP e WebSocket."""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # Thread HTTP
    http_thread = threading.Thread(target=start_http_server, args=(HTTP_PORT,), daemon=True)
    http_thread.start()
    # Loop Asyncio WebSocket
    asyncio.run(start_websocket_server())

# --- GESTIONE INTERFACCIA GRAFICA (GUI) E SYSTEM TRAY ---
root = tk.Tk()
log_widget = None
ip_label_var = None
tray_icon = None

def create_tray_icon():
    """Genera l'icona per la System Tray in runtime."""
    width = 64
    height = 64
    color_bg = (43, 46, 74)   # #2b2e4a
    color_fg = (136, 255, 204) # #88ffcc
    
    image = Image.new('RGB', (width, height), color_bg)
    dc = ImageDraw.Draw(image)
    # Disegna logo stilizzato
    dc.ellipse((10, 10, 54, 54), fill=color_bg, outline=color_fg, width=3)
    dc.ellipse((24, 24, 40, 40), fill=color_fg)
    
    return image

def minimize_to_tray():
    """Nasconde la finestra principale e notifica l'utente."""
    root.withdraw()
    if tray_icon:
        tray_icon.notify("Il server è attivo in background.", "Liquid Mouse")

def restore_window(icon=None, item=None):
    """Ripristina la finestra principale."""
    root.deiconify()
    root.lift()

def terminate_application(icon=None, item=None):
    """Chiude l'applicazione e termina tutti i processi."""
    if icon:
        icon.stop()
    root.quit()
    sys.exit(0)

def run_tray_service():
    """Gestisce il ciclo di vita dell'icona nella System Tray."""
    global tray_icon
    image = create_tray_icon()
    menu = (
        pystray.MenuItem('Apri Pannello', restore_window, default=True),
        pystray.MenuItem('Termina', terminate_application)
    )
    tray_icon = pystray.Icon("LiquidMouse", image, "Liquid Mouse", menu)
    tray_icon.run()

def setup_gui():
    """Configura e costruisce l'interfaccia grafica Tkinter."""
    global log_widget, ip_label_var
    
    root.title("Liquid Mouse - Server Control")
    root.geometry("450x550")
    root.configure(bg=COLOR_BG)
    
    # Override del pulsante di chiusura finestra
    root.protocol("WM_DELETE_WINDOW", minimize_to_tray)

    # Header
    tk.Label(root, text="🖱️ Liquid Mouse", font=("Segoe UI", 20, "bold"), bg=COLOR_BG, fg=COLOR_TEXT).pack(pady=(25, 5))
    tk.Label(root, text="Pannello di Controllo Server", font=("Segoe UI", 10), bg=COLOR_BG, fg=COLOR_ACCENT).pack(pady=(0, 20))

    # Box Informazioni Connessione
    info_frame = tk.Frame(root, bg=COLOR_BG, highlightbackground=COLOR_ACCENT, highlightthickness=1)
    info_frame.pack(padx=40, fill='x')
    
    ip_label_var = tk.StringVar(value="Rilevamento IP...")
    tk.Label(info_frame, textvariable=ip_label_var, font=("Courier New", 14, "bold"), bg=COLOR_BG, fg="white", pady=15).pack()
    tk.Label(info_frame, text="Inserisci questo IP nel dispositivo client", font=("Segoe UI", 8), bg=COLOR_BG, fg="#aaaaaa", pady=5).pack()

    # Area Log
    tk.Label(root, text="Log di Sistema:", font=("Segoe UI", 9, "bold"), bg=COLOR_BG, fg="#dddddd", anchor="w").pack(padx=40, pady=(20, 0), fill='x')
    
    log_widget = scrolledtext.ScrolledText(root, height=10, bg=COLOR_LOG_BG, fg=COLOR_LOG_TEXT, font=("Consolas", 9), relief="flat")
    log_widget.pack(padx=40, pady=5, fill='both', expand=True)

    # Footer
    tk.Label(root, text="Chiudi la finestra per ridurre a icona", font=("Segoe UI", 8), bg=COLOR_BG, fg="#aaaaaa").pack(pady=10)

    # Avvio Thread Servizi
    threading.Thread(target=run_services, daemon=True).start()
    threading.Thread(target=run_tray_service, daemon=True).start()

def log_message(message):
    """Scrive un messaggio thread-safe nell'area di log della GUI."""
    def _write():
        if log_widget:
            from datetime import datetime
            timestamp = datetime.now().strftime("%H:%M:%S")
            log_widget.insert(tk.END, f"[{timestamp}] {message}\n")
            log_widget.see(tk.END)
    root.after(0, _write)

def update_ui_info(ip):
    """Aggiorna l'etichetta dell'IP nell'interfaccia."""
    root.after(0, lambda: ip_label_var.set(f"{ip}:{HTTP_PORT}"))

# --- MAIN ENTRY POINT ---
if __name__ == "__main__":
    setup_gui()
    try:
        root.mainloop()
    except KeyboardInterrupt:
        sys.exit(0)