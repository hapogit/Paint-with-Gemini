# Liquid Mouse Pro - Configurazione

Questo file contiene informazioni sulla struttura del progetto e come configurarlo.

## 📦 Cosa è Incluso

```
liquid-mouse-pro/
├── 📄 README.md                 # Guida completa di installazione
├── 📄 LICENSE                   # Licenza MIT
├── 📄 requirements.txt           # Dipendenze Python
├── 📄 CONTRIBUTING.md            # Guida per contribuire
├── 📄 CHANGELOG.md               # Storico delle versioni
├── 📄 .gitignore                 # File da ignorare in Git
│
├── 🐍 server.py                 # Server WebSocket (Backend)
├── 🌐 index.html                # Interfaccia Web (Frontend)
│
├── ⚙️ start.bat                 # Script automatico (Windows)
├── 🧪 test.py                   # Script di diagnostica
└── 📋 MANIFEST.md               # Questo file
```

## 🚀 Quick Start

### Windows
```powershell
# 1. Doppio clic su start.bat
# Oppure nel terminale:
python server.py
```

### macOS / Linux
```bash
# 1. Installa dipendenze
pip install -r requirements.txt

# 2. Avvia il server
python server.py

# 3. Apri il browser su http://localhost:8000
# Da smartphone: http://[TUO-IP]:8000
```

## 📋 Requisiti Minimi

- Python 3.7 o superiore
- Browser moderno (Chrome, Safari, Edge)
- Smartphone con WiFi

## 🔧 Componenti Principali

### Backend (server.py)
- **Tecnologia**: Python + AsyncIO + WebSockets
- **Porta**: 8765 (WebSocket)
- **HTTP Server**: Porta 8000
- **Funzioni**: Controllo mouse/tastiera tramite WebSocket

### Frontend (index.html)
- **Tecnologia**: HTML5 + CSS3 + JavaScript Vanilla
- **Design**: Glassmorphism moderno
- **Responsive**: Ottimizzato per smartphone
- **WebSocket Client**: Comunicazione con il server

## 📊 Architettura

```
┌─────────────────────────────────────────────────┐
│         SMARTPHONE (Browser)                     │
│                                                 │
│  ┌─────────────────────────────────────────┐   │
│  │  HTML5 Interface (index.html)           │   │
│  │                                         │   │
│  │  - Touchpad                            │   │
│  │  - Bottoni (Click L/R)                │   │
│  │  - Tastiera Virtuale                  │   │
│  │  - Indicatore Connessione             │   │
│  └─────────────────────────────────────────┘   │
└──────────────────┬──────────────────────────────┘
                   │ WebSocket
                   │ (ws://IP:8765)
                   ↓
┌─────────────────────────────────────────────────┐
│      COMPUTER SERVER (server.py)                │
│                                                 │
│  ┌─────────────────────────────────────────┐   │
│  │  WebSocket Server (asyncio)             │   │
│  │  - Riceve comandi JSON                  │   │
│  │  - Invia stato della connessione       │   │
│  └─────────────────────────────────────────┘   │
│            ↓                                    │
│  ┌─────────────────────────────────────────┐   │
│  │  PyAutoGUI (Automazione SO)             │   │
│  │  - Movimento mouse                      │   │
│  │  - Click del mouse                      │   │
│  │  - Input tastiera                       │   │
│  └─────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
```

## 💾 Dipendenze Python

| Pacchetto | Versione | Uso |
|-----------|----------|-----|
| websockets | 14.1 | Server/Client WebSocket |
| pyautogui | 0.9.53 | Automazione mouse/tastiera |

Installa con: `pip install -r requirements.txt`

## ⚙️ Variabili di Configurazione

Nel file `server.py`:

```python
SENSITIVITY = 1.8      # Sensibilità mouse (0.5-5.0)
PORT = 8765            # Porta WebSocket
HTTP_PORT = 8000       # Porta server HTTP
```

Nel file `index.html`:

```css
--bg-color: #2b2e4a;   /* Colore sfondo */
--shadow-out: ...      /* Ombra 3D */
--shadow-in: ...       /* Ombra interna */
```

## 🔗 Protocollo di Comunicazione

### Messaggio Client → Server (JSON)

```json
{
  "type": "move",
  "x": 10.5,
  "y": -5.2
}
```

**Tipi disponibili:**
- `move`: Movimento mouse (x, y in pixel)
- `click`: Click mouse (btn: "left", "right")
- `text`: Input testo (char: "a")
- `key`: Tasto speciale (key: "enter")

### Messaggio Server → Client (JSON)

```json
{
  "status": "connected",
  "ip": "192.168.1.100"
}
```

## 🧪 Testing

```bash
# Verifica sintassi Python
python -m py_compile server.py

# Esegui test diagnostici
python test.py

# Testa manualmente
python server.py
# Apri browser: http://localhost:8000
```

## 📝 Struttura HTML

```html
<!DOCTYPE html>
<html>
  <head>
    <!-- Meta, CSS -->
  </head>
  <body>
    <!-- Pannello Configurazione (nascosto dopo connessione) -->
    <!-- Pannello Controllo (Touchpad, Bottoni, Tastiera) -->
    <!-- Script WebSocket -->
  </body>
</html>
```

## 🎨 Design System

**Colori:**
- Background: #2b2e4a (Blu scuro)
- Glass: rgba(255,255,255,0.03) (Trasparente)
- Accent: Vari per bottoni

**Tipografia:**
- Font: Sistema (San Francisco, Segoe UI, ecc.)
- Responsive: Adatta a varie dimensioni

**Ombra:**
- Neuromorphic: 3D convesso/concavo
- Glassmorphism: Effetto vetro soffiato

## 🚀 Deployment

### Su rete locale
1. Esegui `python server.py`
2. Appunta l'IP mostrato
3. Da smartphone: `http://[IP]:8000`

### Su server remoto
⚠️ **ATTENZIONE**: Aggiungi SSL/TLS e autenticazione

```python
# Pseudocodice per deployment sicuro
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain("cert.pem", "key.pem")
# server = await websockets.serve(..., ssl=ssl_context)
```

## 📚 Letture Aggiuntive

- [WebSockets su Python](https://websockets.readthedocs.io/)
- [PyAutoGUI Docs](https://pyautogui.readthedocs.io/)
- [MDN Web Socket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)

## 🐛 Segnalare Bug

Se trovi un problema:
1. Esegui `python test.py`
2. Controlla i log del server
3. Prova su un diverso browser/dispositivo
4. Segnala il bug con dettagli

## 📄 Licenza

MIT - Vedi LICENSE per i dettagli

---

**Versione**: 1.0.0  
**Data**: Gennaio 2026
