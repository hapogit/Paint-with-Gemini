# INSTALLAZIONE E SETUP

Questo documento descrive come installare e configurare Liquid Mouse Pro.

## 🖥️ Sistema Operativo Supportati

- ✅ Windows 10 / 11
- ✅ macOS (Intel e Apple Silicon)
- ✅ Linux (Ubuntu, Debian, Fedora, ecc.)

## 📋 Prerequisiti

1. **Python 3.7+**
   - Scarica da: https://python.org
   - ✅ Assicurati di spuntare "Add Python to PATH" durante l'installazione

2. **Smartphone con browser**
   - iOS: Safari
   - Android: Chrome, Firefox, Opera

3. **Connessione WiFi**
   - Computer e smartphone sulla stessa rete

## ⚡ Installazione Rapida (Windows)

```batch
# 1. Apri PowerShell/CMD nella cartella del progetto
# 2. Esegui:
python -m pip install --upgrade pip
pip install -r requirements.txt

# 3. Avvia il server:
python server.py

# 4. Dal telefono apri il link mostrato nel terminale
```

## 🍎 Installazione su macOS

```bash
# Usa Homebrew per Python (consigliato)
brew install python3

# O scarica da python.org

# Poi:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Avvia:
python3 server.py
```

## 🐧 Installazione su Linux

```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv

# Fedora
sudo dnf install python3 python3-pip

# Poi:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Avvia:
python3 server.py
```

## 🔍 Verifica dell'Installazione

Esegui lo script di verifica:

**Windows:**
```batch
python verify.py
REM Oppure:
verify.bat
```

**macOS/Linux:**
```bash
python3 test.py
```

## 🚀 Primo Avvio

1. **Apri il terminale** nella cartella del progetto

2. **Esegui il server:**
   ```bash
   python server.py
   # o
   python3 server.py
   ```

3. **Vedrai un output come questo:**
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

4. **Annota l'IP** (nel nostro esempio: `192.168.1.100`)

5. **Dal tuo smartphone:**
   - Apri il browser (Safari su iOS, Chrome su Android)
   - Digita: `http://192.168.1.100:8000` (sostituisci con il tuo IP)
   - Premi Invio

6. **Nella finestra di configurazione:**
   - L'IP dovrebbe essere già compilato
   - Se non è corretto, modificalo
   - Premi il pulsante **CONNETTI**

7. **Quando vedi "LINKED" in verde**, sei connesso! 🎉

## 🔧 Configurazione Post-Installazione

### Sensibilità del Mouse

Modifica il valore `SENSITIVITY` in `server.py`:

```python
SENSITIVITY = 1.8  # Valore predefinito
```

- **Aumentare** (es: 2.5) = Mouse più veloce
- **Diminuire** (es: 0.8) = Mouse più lento

### Porte Personalizzate

Se le porte 8765 o 8000 sono occupate, modificale in `server.py`:

```python
PORT = 8765        # Cambia il numero se occupato
HTTP_PORT = 8000   # Cambia il numero se occupato
```

### Tema e Colori

Nel file `index.html`, modifica la sezione `:root`:

```css
:root {
    --bg-color: #2b2e4a;                     /* Blu scuro */
    --glass-surface: rgba(255,255,255,0.03); /* Trasparenza */
    --text-subtle: rgba(255,255,255,0.3);    /* Testo */
}
```

## 🐛 Troubleshooting Installazione

### "Python non trovato"

**Soluzione:**
1. Scarica Python da https://python.org
2. Durante l'installazione, **spunta** "Add Python to PATH"
3. Riavvia il computer
4. Prova di nuovo

### "ModuleNotFoundError: No module named 'websockets'"

**Soluzione:**
```bash
pip install websockets pyautogui
```

### "Porta 8765 già in uso"

**Soluzione:**
```bash
# Windows
netstat -ano | findstr :8765
taskkill /PID <numero> /F

# macOS/Linux
lsof -i :8765
kill -9 <numero>
```

### "ModuleNotFoundError: No module named 'pyautogui'"

**Soluzione:**
```bash
pip install pyautogui
```

## 📱 Accesso da Smartphone

### 🔗 URL Corrette

- Stesso dispositivo (debug): `http://localhost:8000`
- Stessa rete: `http://192.168.1.100:8000`
- Rete diversa: Aggiungi SSL/TLS (vedi MANIFEST.md)

### 🌐 Browser Compatibili

| Browser | iOS | Android | Note |
|---------|-----|---------|------|
| Safari | ✅ | - | iOS 13+ |
| Chrome | ✅ | ✅ | Consigliato |
| Firefox | ⚠️ | ✅ | Possibili problemi su iOS |
| Edge | ❌ | ✅ | Non testato su iOS |
| Opera | ❌ | ✅ | Funziona |

## ✅ Checklist di Verifica

Prima di iniziare a usarlo:

- [ ] Python 3.7+ installato e nel PATH
- [ ] `pip install -r requirements.txt` completato senza errori
- [ ] `python test.py` mostra ✅ per tutto
- [ ] Server avvia senza errori (`python server.py`)
- [ ] Riesci ad accedere a `http://localhost:8000` dal computer
- [ ] Riesci ad accedere da smartphone alla stessa rete
- [ ] La connessione mostra "LINKED" in verde

## 🎓 Prossimi Passi

Una volta installato:

1. Leggi il [README.md](README.md) per l'utilizzo completo
2. Modifica la [Configurazione Avanzata](MANIFEST.md#-configurazione-avanzata)
3. Consulta [CONTRIBUTING.md](CONTRIBUTING.md) se vuoi contribuire

## 📚 Risorse Utili

- [Documentazione Python](https://docs.python.org/)
- [WebSockets Library](https://websockets.readthedocs.io/)
- [PyAutoGUI Reference](https://pyautogui.readthedocs.io/)
- [MDN WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)

---

**Tutto installato? Inizia a usarlo seguendo il [README.md](README.md)!**
