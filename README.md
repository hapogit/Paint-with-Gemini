# 🖱️ Liquid Mouse v1.5.0

> **Trasforma il tuo smartphone in un touchpad wireless fluido e professionale.**
> Nessuna installazione richiesta. Scarica, esegui, controlla.

Liquid Mouse è un'applicazione portatile che opera interamente sulla tua rete Wi-Fi locale, garantendo privacy e velocità.

## ✨ Funzionalità Principali

* **Zero Installazione:** Basta avviare l'eseguibile per iniziare.
* **Fluid Touch:** Movimento del cursore a bassa latenza.
* **Smart Menu:** Menu centrale a comparsa con strumenti rapidi e Clipboard (Copia/Incolla).
* **Smart Scrolling:** Scorrimento inerziale ad alta sensibilità.
* **Productivity Tools:** Drag & Drop, Seleziona Tutto (Ctrl+A), Tastiera Remota.
* **Terminal GUI:** Interfaccia server moderna in stile terminale con supporto System Tray.
* **Privacy First:** Nessun cloud. I dati rimangono nella tua rete locale.

---

## 🚀 Istruzioni Rapide (Windows)

Liquid Mouse per Windows è **standalone**. Non hai bisogno di installare Python o altri software.

### 1. Avvia
Scarica il file ed esegui **`LiquidMouse.exe`**.
*(Suggerimento: Puoi spostarlo dove vuoi, anche su una chiavetta USB).*

### 2. Connetti
All'avvio vedrai una finestra nera e verde con i dati di connessione:
1. Assicurati che il PC e lo smartphone siano collegati allo **stesso Wi-Fi**.
2. Scansiona il QR Code (se disponibile) o apri il browser del telefono.
3. Digita l'indirizzo mostrato (es: `http://192.168.1.x:8000`).

### 3. Usa
Quando lo schermo del telefono diventa verde (**LINKED**), sei pronto!

---

## 🖥️ macOS & Linux (Esecuzione da Sorgente)

Poiché l'eseguibile `.exe` è specifico per Windows, gli utenti macOS e Linux possono avviare l'app tramite Python:

```bash
# 1. Clona o scarica la repository
# 2. Installa le dipendenze
pip3 install -r requirements.txt

# 3. Avvia il server
python3 server.pyw
