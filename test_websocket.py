from seleniumbase import SB

# Usa mitmproxy locale come proxy (forza tutto il traffico)
PROXY = "http://localhost:8080"

print("🚀 Test WebSocket con mitmproxy...")

with SB(uc=True, headless=True, xvfb=True, proxy=PROXY) as sb:
    # Test 1: IP
    sb.open("https://api.ipify.org")
    ip = sb.get_text("body")
    print(f"✅ IP del browser: {ip}")
    
    # Test 2: EasyHits4U
    sb.open("https://www.easyhits4u.com/logon/")
    print(f"📍 Titolo: {sb.get_title()}")
    
    # Se arrivi qui, il proxy funziona
    print("🎉 Successo! Il browser ha caricato la pagina attraverso il proxy.")