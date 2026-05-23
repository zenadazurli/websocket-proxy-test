from seleniumbase import SB

PROXY = "http://localhost:8080"

print("🚀 Test WebSocket con mitmproxy...")

with SB(uc=True, headless=True, xvfb=True, proxy=PROXY) as sb:
    sb.open("https://api.ipify.org")
    ip = sb.get_text("body")
    print(f"✅ IP del browser: {ip}")
    
    sb.open("https://www.easyhits4u.com/logon/")
    print(f"📍 Titolo: {sb.get_title()}")
    
    print("🎉 Successo! Il browser ha caricato la pagina attraverso il proxy.")
