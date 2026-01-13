# 🖱️ Liquid Mouse Pro

Controlla il mouse e la tastiera del tuo computer direttamente dal tuo smartphone. Un'applicazione moderna e fluida basata su WebSocket.

**Status**: ✅ Stabile e pronto all'uso  
**Licenza**: MIT  
**Versione**: 1.0.0

---

## 📋 Indice

- [Requisiti](#-requisiti)
- [Installazione](#-installazione-e-avvio)
- [Utilizzo](#-utilizzo)
- [Configurazione](#-configurazione-avanzata)
- [Troubleshooting](#-troubleshooting)
- [Licenza](#-licenza)

---

## ⚙️ REQUISITI

- **Computador**: Windows, macOS o Linux con Python 3.7+
- **Smartphone**: Browser moderno (iOS Safari / Android Chrome)
- **Rete**: Computer e smartphone connessi alla **STESSA rete WiFi**
- **Porte**: 8765 (WebSocket) e 8000 (HTTP) disponibili

---

## 🚀 INSTALLAZIONE E AVVIO

### Metodo 1: Script Automatico (Windows)

Se usi Windows, fai doppio clic su `start.bat`. Lo script farà tutto automaticamente:
- ✅ Verifica Python
- ✅ Installa le dipendenze
- ✅ Avvia il server

### Metodo 2: Manuale

#### 1️⃣ INSTALLA LE DIPENDENZE

Apri il Terminale/PowerShell nella cartella del progetto e digita:

```bash
pip install -r requirements.txt
```

Oppure manualmente:

```bash
pip install websockets pyautogui
```

#### 2️⃣ VERIFICA LA CONFIGURAZIONE (Opzionale)

```bash
python test.py
```

Questo script verificherà:
- ✅ Connettività di rete
- ✅ Disponibilità delle porte
- ✅ Configurazione IP

#### 3️⃣ AVVIA IL SERVER

Sempre nel terminale:

```bash
python server.py
```

Vedrai qualcosa come:

```
==================================================
   🖱️  LIQUID MOUSE SERVER
==================================================
📡 IP Locale: 192.168.1.100
🔌 Porta: 8765
🌐 WebSocket: ws://192.168.1.100:8765
==================================================

📱 Apri questo link sul tuo smartphone:
   http://192.168.1.100:8000

⏳ In attesa di connessione...
==================================================
```

**ANNOTA L'IP MOSTRATO** (es: `192.168.1.100`)

---

---

## 📱 COLLEGAMENTO DA SMARTPHONE

### Opzione 1: Server HTTP (Consigliato)

Dal tuo smartphone apri il browser e digita:

```
http://[IP-DEL-COMPUTER]:8000
```

Esempio:
```
http://192.168.1.100:8000
```

### Opzione 2: File Locale
1. Scarica il file `index.html` sul tuo smartphone
2. Apri il browser e seleziona il file
3. Inserisci l'IP del computer nel campo di configurazione
4. Premi **CONNETTI**

---

## 🎮 UTILIZZO

Una volta connesso (vedrai "LINKED" in verde):

| Azione | Descrizione |
|--------|-------------|
| **Touchpad** | Tocca e trascinale dito per spostare il mouse |
| **Tasto L** | Click sinistro del mouse |
| **Tasto R** | Click destro del mouse |
| **Tasto Tastiera** | Apre la tastiera virtuale per scrivere |
| **Tasto Invio** | Invia il tasto Enter |

---

## 🔧 CONFIGURAZIONE AVANZATA

### Sensibilità del Mouse

Nel file `server.py` modifica:

```python
SENSITIVITY = 1.8  # Aumenta per mouse più veloce (es: 2.5)
                   # Diminuisci per mouse più lento (es: 0.8)
```

### Porte Personalizzate

```python
PORT = 8765          # Porta WebSocket
HTTP_PORT = 8000     # Porta HTTP
```

### Tema Colori

Nel file `index.html` modifica la sezione CSS `:root`:

```css
:root {
    --bg-color: #2b2e4a;                          /* Sfondo */
    --glass-surface: rgba(255, 255, 255, 0.03);   /* Trasparenza */
    --text-subtle: rgba(255, 255, 255, 0.3);      /* Testo */
}
```

---

## 🐛 TROUBLESHOOTING

### "Porta 8765 già in uso"

**Windows:**
```bash
netstat -ano | findstr :8765
taskkill /PID <PID> /F
```

**Linux/Mac:**
```bash
lsof -i :8765
kill -9 <PID>
```

### "Non riesco a connettermi dal telefono"

1. ✅ Verifica di essere sulla **stessa rete WiFi**
2. ✅ Disabilita temporaneamente il firewall
3. ✅ Controlla che l'IP mostrato dal server sia corretto
4. ✅ Esegui `python test.py` per diagnosticare

### "Il server non parte"

```bash
python test.py
```

Lo script mostrerà il problema specifico.

### "Mouse lento/veloce"

Modifica `SENSITIVITY` in `server.py` (vedi sopra).

### "La tastiera non funziona"

- Assicurati di aver toccato il pulsante tastiera
- Verifica che lo smartphone abbia un input method abilitato
- Alcuni caratteri speciali potrebbero non essere supportati

---

## 📂 Struttura del Progetto

```
liquid-mouse-pro/
├── server.py              # Server WebSocket principale
├── index.html             # Interfaccia web (smartphone)
├── start.bat              # Script automatico (Windows)
├── test.py                # Test diagnostico
├── requirements.txt       # Dipendenze Python
├── README.md              # Questo file
├── LICENSE                # Licenza MIT
└── CONTRIBUTING.md        # Guida per contribuire
```

---

## 🛡️ SICUREZZA

⚠️ **ATTENZIONE**: Questo server gira sulla tua rete locale **SENZA crittografia**.

**Non usare su reti pubbliche o non sicure!**

Per uso in produzione, considera di aggiungere:
- 🔐 SSL/TLS al WebSocket
- 🔑 Autenticazione con token
- 🚪 Firewall locale

---

## 🤝 CONTRIBUIRE

Vuoi migliorare il progetto? Leggi [CONTRIBUTING.md](CONTRIBUTING.md)

**Idee di miglioramento:**
- Supporto per più dispositivi simultaneamente
- Interfaccia web migliorata
- Supporto per gesti avanzati
- Compatibilità con browser più datati
- Supporto per mouse gaming (side buttons)

---

## 📄 LICENZA

Questo progetto è distribuito con licenza **MIT**.  
Vedi [LICENSE](LICENSE) per i dettagli completi.

Sei libero di:
- ✅ Usare il software per scopi personali e commerciali
- ✅ Modificare e distribuire il codice
- ✅ Creare derivati

Basta mantenere l'attribuzione originale.

---

## 💬 SUPPORTO

Per problemi o domande:
1. Controlla la sezione [Troubleshooting](#-troubleshooting)
2. Esegui `python test.py`
3. Leggi i commenti nel codice
4. Apri un'issue su GitHub

---

## 🚀 TECH STACK

- **Frontend**: HTML5 + CSS3 + JavaScript Vanilla
- **Backend**: Python + Asyncio + WebSockets
- **Automazione**: PyAutoGUI per input del sistema operativo
- **Protocollo**: WebSocket con JSON

---

**Fatto con ❤️ per il controllo remoto fluido e intuitivo.** 
