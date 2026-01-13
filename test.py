"""
Script di test per verificare che il server Liquid Mouse funzioni correttamente
"""
import socket
import sys

def test_network():
    """Testa la configurazione di rete"""
    print("🔧 TEST DI CONNESSIONE LIQUID MOUSE")
    print("=" * 50)
    
    # Test 1: IP locale
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        print(f"✅ IP Locale: {ip}")
    except Exception as e:
        print(f"❌ Errore nel rilevare l'IP: {e}")
        return False
    
    # Test 2: Porta disponibile
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 8765))
        s.close()
        print(f"✅ Porta 8765: Disponibile")
    except:
        print(f"❌ Porta 8765: Occupata (ferma il server precedente)")
        return False
    
    print("=" * 50)
    print("\n📱 PROCEDURA DI COLLEGAMENTO:")
    print(f"1. Avvia il server: python server.py")
    print(f"2. Dal tuo smartphone, apri: http://{ip}:8000")
    print(f"3. Inserisci l'IP: {ip}")
    print(f"4. Premi CONNETTI")
    print("\n✅ Tutto OK! Puoi procedere.")
    return True

if __name__ == "__main__":
    if not test_network():
        sys.exit(1)
