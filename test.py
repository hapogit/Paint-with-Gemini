"""
Script di diagnostica per Liquid Mouse
Verifica rete, porte e dipendenze.
"""
import socket
import sys
import importlib.util

def check_dependencies():
    """Controlla se le librerie necessarie sono installate"""
    required = ['websockets', 'pyautogui', 'pystray', 'PIL']
    missing = []
    print("📦 VERIFICA DIPENDENZE:")
    for package in required:
        if importlib.util.find_spec(package) is None and importlib.util.find_spec("PIL" if package == "Pillow" else package) is None:
            print(f"   ❌ {package} mancante")
            missing.append(package)
        else:
            print(f"   ✅ {package} OK")
    
    if missing:
        print(f"\n⚠️  Esegui: pip install -r requirements.txt")
        return False
    return True

def test_network():
    """Testa la configurazione di rete"""
    print("\n🔧 TEST DI RETE:")
    
    # Test 1: IP locale
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        print(f"   ✅ IP Locale rilevato: {ip}")
    except Exception as e:
        print(f"   ❌ Errore rilevamento IP: {e}")
        return False, None
    
    # Test 2: Porta disponibile
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 8765))
        s.close()
        print(f"   ✅ Porta 8765 (WebSocket): Disponibile")
    except:
        print(f"   ❌ Porta 8765: Occupata (Il server è già attivo?)")
        # Non è necessariamente un errore fatale se l'utente sta testando col server acceso
    
    return True, ip

if __name__ == "__main__":
    print("=" * 50)
    print("   🔍 LIQUID MOUSE - DIAGNOSTICA")
    print("=" * 50)
    
    deps_ok = check_dependencies()
    net_ok, ip = test_network()
    
    print("=" * 50)
    if deps_ok and net_ok:
        print("\n✅ SISTEMA PRONTO!")
        print("\n🚀 COME AVVIARE:")
        print(f"   1. Doppio click su 'start.bat' (o esegui 'pythonw server.pyw')")
        print(f"   2. L'icona apparirà nella System Tray (in basso a destra)")
        print(f"   3. Dal telefono apri: http://{ip}:8000")
    else:
        print("\n❌ CI SONO PROBLEMI DA RISOLVERE.")
    
    print("\nPremi Invio per uscire...")
    input()