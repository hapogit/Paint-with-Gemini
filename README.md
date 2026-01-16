# 🖱️ Liquid Mouse v1.6.0 (Portable Edition)

Liquid Mouse trasforma il tuo smartphone in un touchpad wireless fluido e professionale per il tuo computer, operante interamente sulla rete Wi-Fi locale.

> **Novità:** Ora disponibile come applicazione portatile per Windows! Nessuna installazione richiesta.

## ✨ Funzionalità Principali

* **Fluid Touch:** Movimento del cursore a bassa latenza.
* **Smart Menu:** Menu centrale a comparsa con strumenti rapidi e Clipboard (Copia/Incolla).
* **Smart Scrolling:** Scorrimento inerziale ad alta sensibilità.
* **Funzioni Avanzate:** Drag & Drop, Seleziona Tutto (Ctrl+A), Tastiera Remota.
* **Server GUI:** Interfaccia moderna con supporto System Tray e Icone Personalizzate.
* **Privacy First:** Nessun cloud, funziona solo sulla rete locale.
* **Portable:** Esegui direttamente senza installare nulla (solo Windows).

## ⚠️ Limitazioni Importanti

* **Schermata di Login/Blocco:** A causa delle restrizioni di sicurezza di Windows (Secure Desktop), l'applicazione **non può interagire** con la schermata di login o quando il PC è bloccato. È necessario utilizzare un mouse/tastiera fisica per inserire la password. Una volta effettuato l'accesso, Liquid Mouse inizierà a funzionare immediatamente.

## 🚀 Avvio Rapido (Windows)

Il modo più semplice per usare Liquid Mouse. Nessuna competenza tecnica richiesta.

### 1. Download ed Esecuzione
1.  Scarica il file **`LiquidMouse.exe`** dalla cartella `dist` o dalle Release.
2.  Fai doppio click su **`LiquidMouse.exe`**.
3.  L'applicazione si avvierà mostrando una finestra stile terminale con il tuo indirizzo IP.

> *Nota: Windows Defender potrebbe mostrare un avviso poiché l'app non è firmata digitalmente. Clicca su "Ulteriori informazioni" -> "Esegui comunque".*

### 2. Connessione da Smartphone
1.  Assicurati che il tuo telefono sia collegato allo **stesso Wi-Fi** del PC.
2.  Leggi l'indirizzo IP mostrato nella finestra di Liquid Mouse (es: `192.168.1.100:8000`).
3.  Apri il browser del telefono (Chrome/Safari) e digita quell'indirizzo.
4.  Premi **CONNETTI**.

## 🛠️ Installazione Manuale (macOS / Linux / Sviluppatori)

Segui questa procedura se usi macOS, Linux o se vuoi modificare il codice sorgente Python.

### 📋 Prerequisiti
* **Python 3.7+** installato
* Connessione Wi-Fi condivisa

### 🍎 macOS / 🐧 Linux

```bash
# 1. Clona o scarica il progetto
git clone [https://github.com/tuoutente/liquid-mouse.git](https://github.com/tuoutente/liquid-mouse.git)
cd liquid-mouse

# 2. Crea ambiente virtuale (consigliato)
python3 -m venv venv
source venv/bin/activate

# 3. Installa dipendenze
pip install -r requirements.txt

# 4. Avvia il server
python3 server.pyw

🖥️ Windows (Metodo Python)Se preferisci usare lo script Python invece dell'EXE:

Snippet di codice

python -m pip install --upgrade pip
pip install -r requirements.txt
python server.pyw

⚙️ Configurazione Avanzata
Anche con la versione EXE, puoi configurare alcune opzioni se scarichi il pacchetto completo. Se stai usando solo l'.exe, queste impostazioni sono predefinite.

Sensibilità del MousePer modificare la sensibilità, è necessario utilizzare la versione Python (server.pyw) e modificare la variabile:

Python

SENSITIVITY = 1.8  # Default

Porte Personalizzate

Se la porta 8765 è occupata, l'applicazione non si avvierà. Chiudi l'applicazione che usa quella porta o modifica PORT nel file sorgente server.pyw e ricompila.

📱 Browser Compatibili

Browser iOS Android Note Safari✅-Consigliato su iOSChrome✅✅Consigliato su AndroidFirefox⚠️✅Possibili problemi su iOSOpera❌✅Funziona

📜 Changelog

[1.6.0] - 2026-01-17 (Portable Edition)

✨ Novità

Standalone EXE: Rilasciato LiquidMouse.exe. Il programma è ora completamente portatile e non richiede l'installazione di Python per l'utente finale.

Builder: Aggiunto script build.py per automatizzare la creazione dell'eseguibile.

[1.5.0] - 2026-01-17 (Terminal Edition)

✨ Novità

Terminal GUI: Nuova interfaccia server in stile terminale virtuale con animazioni di boot.

[1.4.0] - 2026-01-16 (Smart Menu Edition)

✨ Novità

Smart Menu: Nuovo pulsante centrale che apre un menu a raggiera.

Clipboard: Aggiunti pulsanti Copia (Ctrl+C) e Incolla (Ctrl+V).

📄 Licenza

Distribuito sotto licenza MIT. Vedi LICENSE per maggiori informazioni.
